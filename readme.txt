# Desafio LizardTI - PDF e IA Generativa com Gemini

    - Este projeto implementa uma API que permite fazer upload de um arquivo PDF, processá-lo usando uma IA generativa (Gemini) e responder 
    a perguntas do usuário sobre o conteúdo do PDF.
    - Através de engenharia de prompt, as respostas da IA são fornecidas em formato JSON.
    - Os resultados são armazenados em um banco de dados NoSQL (MongoDB). 


## Requisitos

- Antes de começar, certifique-se de ter instalado os seguintes requisitos:

    1. **Python 3.8 ou superior**
    2. **Google Colab** (opcional, caso queira rodar a IA diretamente na nuvem)
    3. **MongoDB** (local ou Atlas, para armazenamento dos resultados)
    4. **FastAPI** e outras bibliotecas Python listadas no arquivo `requirements.txt`

### Passo 1: Clonar o repositório

    Faça o clone do repositório do GitHub:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

### Passo 2: Configurar o ambiente virtual

    Para evitar conflitos de dependências, crie e ative um ambiente virtual Python:

    ```bash

    # Crie o ambiente virtual
        python -m venv venv

    # Ative o ambiente virtual
    # No Windows:
        venv\Scripts\activate

    # No macOS/Linux:
    source venv/bin/activate
    ```

### Passo 3: Instalar as dependências

    Instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Passo 4: Configurar variáveis de ambiente

    Crie um arquivo `.env` na raiz do projeto para armazenar suas credenciais sensíveis, como a chave da API do Gemini e a URL do MongoDB.

    Exemplo de conteúdo do `.env`:

    ```bash
    GEMINI_API_KEY="sua-chave-api-do-gemini"
    MONGODB_URI="sua-url-do-mongodb"
    ```

### Passo 5: Executar o servidor FastAPI

    Agora que tudo está configurado, você pode iniciar o servidor FastAPI para receber as requisições de upload de PDF.

    ```bash
    # Executar o servidor FastAPI
    uvicorn main:app --reload
    ```

    - O servidor estará rodando em `http://127.0.0.1:8000`.

### Passo 6: Fazer upload de um arquivo PDF e enviar perguntas

    Para testar a API, você deve utilizar a ferramenta própria da FastAPI. Acesse: "http://127.0.0.1:8000/docs"

    Faça o upload dos arquivos fornecidos como exemplo e faça uma pergunta para a IA via terminal. 
    A IA respondera um JSON com sua pergunta e outros dados gerais sobre o contrato

    A resposta da API será o JSON gerado pela IA com base no conteúdo do PDF e na pergunta feita.

### Passo 7: Verificar os dados no MongoDB

    Após processar a pergunta, a resposta será armazenada no MongoDB. Para visualizar as informações armazenadas, você pode usar a interface do MongoDB ou qualquer cliente de banco de dados NoSQL.

    ---

## Dependências

    As principais dependências do projeto incluem:

    - `FastAPI`: Framework para a criação da API.
    - `PyPDF2`: Para leitura e extração de texto dos arquivos PDF.
    - `pymongo`: Para interação com o MongoDB.
    - `google.generativeai`: Biblioteca de integração com a API do Gemini.

### Como instalar as dependências manualmente:

    Caso você prefira instalar manualmente cada uma das dependências:

    ```bash
    pip install fastapi uvicorn pydantic PyPDF2 pymongo python-dotenv google-generativeai
    ```

---

## Testes

    Para testar o projeto localmente, você pode usar os PDFs de exemplo fornecidos no repositório ou seus próprios arquivos PDF.

---

## Conclusão

    Este projeto demonstra como utilizar FastAPI com uma IA generativa para processar arquivos PDF, com foco em engenharia de prompts para garantir 
    respostas estruturadas em JSON. Se você tiver dúvidas ou problemas, consulte a documentação das bibliotecas ou abra uma issue no repositório.





##### Contato:
    Rigel Sales
    rigelsouza@gmail.com
    +5583996461138




#### About me:
https://www.linkedin.com/in/rigel-sales-847278292/