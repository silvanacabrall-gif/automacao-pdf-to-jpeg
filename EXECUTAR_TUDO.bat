@echo off
echo [1/2] Iniciando Extração e Unificação de PDFs...
python src/extrair_pdfs.py
echo.
echo [2/2] Iniciando Conversão para Imagem (JPEG)...
python src/pdf_to_jpeg.py
echo.
echo ✅ Processo concluído com sucesso!
pause