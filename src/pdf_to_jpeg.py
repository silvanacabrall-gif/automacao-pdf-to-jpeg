import os
from pdf2image import convert_from_path

# Define os caminhos base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_pdfs = os.path.join(BASE_DIR, 'saida_pdfs')
pasta_saida_img = os.path.join(BASE_DIR, 'saida_imagens')

caminho_poppler = r'C:\Users\nex-i\OneDrive\Documentos\Documentos_importantes\POPPLER\poppler-24.08.0\Library\bin'

os.makedirs(pasta_saida_img, exist_ok=True)

if not os.path.exists(pasta_pdfs):
    print(f"⚠️ Pasta não encontrada: {pasta_pdfs}")
else:
    arquivos = [f for f in os.listdir(pasta_pdfs) if f.lower().endswith('.pdf')]
    
    if not arquivos:
        print("⚠️ Nenhum PDF encontrado para converter.")
    else:
        for arquivo in arquivos:
            print(f"🖼️ Convertendo: {arquivo}")
            caminho_pdf = os.path.join(pasta_pdfs, arquivo)
            
            try:
                # Tentamos converter passando o caminho do poppler explicitamente
                imagens = convert_from_path(caminho_pdf, poppler_path=caminho_poppler)
                
                for i, img in enumerate(imagens):
                    nome_img = f"{os.path.splitext(arquivo)[0]}_pag_{i+1}.jpg"
                    caminho_final = os.path.join(pasta_saida_img, nome_img)
                    img.save(caminho_final, 'JPEG')
            except Exception as e:
                print(f"❌ Erro ao converter {arquivo}: {e}")
        
        print(f"✅ Sucesso! Verifique a pasta: {pasta_saida_img}")