import os
import shutil

# Define os caminhos base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_mae = os.path.join(BASE_DIR, 'entrada')
pasta_destino = os.path.join(BASE_DIR, 'saida_pdfs')

os.makedirs(pasta_destino, exist_ok=True)

print(f"🔍 Buscando em: {pasta_mae}")

contador = 0
for root, dirs, files in os.walk(pasta_mae):
    for arquivo in files:
        if arquivo.lower().endswith('.pdf'):
            caminho_origem = os.path.join(root, arquivo)
            nome_pasta_pai = os.path.basename(root)
            novo_nome = f"{nome_pasta_pai}_{arquivo}"
            caminho_destino = os.path.join(pasta_destino, novo_nome)
            
            shutil.copy2(caminho_origem, caminho_destino)
            contador += 1
            print(f"✅ Extraído: {novo_nome}")

print(f"\n🎉 Total: {contador} PDFs unificados com sucesso!")