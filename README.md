## Descrição
Esse script automatiza o processo de scraping de uma tabela web usando Selenium, filtra faturas vencidas ou que vencem hoje, faz download das imagens das faturas, extrai dados via OCR (pytesseract) e gera um CSV com as informações.

## Estrutura do projeto
- `main.py`: Ponto de entrada principal que orquestra o fluxo completo.
- `config.py`: Arquivo de configurações (URLs, caminhos, Tesseract, etc.).
- `web_scraper.py`: Funções para configuração do Selenium e scraping da tabela web.
- `ocr_utils.py`: Utilitários para processamento de OCR nas imagens das faturas.
- `file_utils.py`: Funções para limpeza de arquivos e pastas.
- `requirements.txt`: Dependências Python necessárias.
- `invoices/`: Pasta onde as imagens das faturas são salvas temporariamente.
- `invoices.csv`: Arquivo CSV gerado com os dados extraídos.

## Requisitos
- Python 3.8+
- **Google Chrome** instalado no sistema.
- Bibliotecas Python (veja `requirements.txt`): `requests`, `pillow`, `pytesseract`, `selenium`, `pandas`
- **Tesseract OCR** instalado no sistema e disponível no PATH, ou configure o caminho em `config.py`.
  - Windows: Instalar via instalador oficial (ex.: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
  - Linux/Mac: Instalar via package manager (ex.: `sudo apt install tesseract-ocr`)
  - Download em: https://github.com/UB-Mannheim/tesseract/wiki

## Configuração e Execução
1. **Clonar o repositório**
   ```bash
   git clone https://github.com/romulosousi/rpa-challenge-ocr-azure.git
   cd rpa-challenge-ocr-azure
   ```

2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar Tesseract (se necessário)**
   - Abra `config.py` e ajuste `TESSERACT_CMD` para o caminho do executável do Tesseract, se não estiver no PATH.

4. **Executar o script**
   ```bash
   python main.py
   ```

## Resultado esperado
- Um arquivo `invoices.csv` será gerado na raiz do projeto com o cabeçalho: `ID,DueDate,InvoiceNo,InvoiceDate,CompanyName,TotalDue`.
- **Datas** no formato `DD-MM-YYYY`.
- **TotalDue** com ponto decimal (ex.: `1234.40`).
- Apenas faturas vencidas ou que vencem hoje são processadas.
- Imagens das faturas ficam salvas em `invoices/` para referência.

## Decisões Técnicas
- **Selenium**: Usado para interagir com a página web dinâmica e extrair dados da tabela.
- **OCR com Pytesseract**: Para extrair texto das imagens das faturas.
- **Pandas**: Para manipulação e salvamento do CSV.
- **Modularização**: Código dividido em módulos para melhor organização e manutenção.


