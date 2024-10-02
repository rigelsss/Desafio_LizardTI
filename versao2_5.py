#Imports de biblioteas necessárias

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json, os
from PyPDF2 import PdfReader
from fastapi import FastAPI, UploadFile
from pymongo import MongoClient
from dotenv import load_dotenv


app = FastAPI()                                                     #Inicia-se 'app' como uma instância de FastAPI()
load_dotenv()


#Criando o endpoint na API para o upload de um arquivo PDF

@app.post("/uploadfile/")
async def creat_upload_file(file: UploadFile):
    pdf_reader = PdfReader(file.file)                               #Cria-se uma instância 'pdf_reader' de 'PdfReader' para leitura do PDF
    pdf_content = ""                                                #Inicia-se 'pdf_content' com dados vazios para que todo o texto do PDF seja armazenado no mesmo 
    num_pages = len(pdf_reader.pages)


    for page_number in range(num_pages):                            #Loop que iterage em cada página do PDF, extraindo o texto e adicionando-o a 'pdf_content'
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        pdf_content += text 



    #----------------------------------------Configurações para uso da Gemini AI----------------------------------------------------

    API_KEY = os.getenv('API_KEY')
    MONGO_URI = os.getenv('MONGO_URI')


    #Configuração da chave pessoal de API
    genai.configure(api_key=API_KEY)


    #Ajustes dos parâmetros de amostragem
    generation_config = {
        'temperature': 0,                                           #'temperature':0 -> A resposta selecionada é sempre a de maior probabilidade. É um padrão determinista de geração de texto. 
        'top_k': 0,                                                 #'top_k':0 -> Valor baixo para termos uma geração de respostas menos aleatórias
        'top_p': 0,                                                 #'top_p':1 -> Valor padrão para geração de respostas mais precisas. 
    }


    #Configurações da IA relacionadas a potenciais discursos perigosos. 
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }


    #Escolha do modelo da IA a ser utilizado
    model_name = 'gemini-1.5-flash'


    #Início do modelo a ser utilizado
    model = genai.GenerativeModel(
        model_name = model_name,
        generation_config = generation_config,
        safety_settings = safety_settings
)
    
    #Inicio do chat com a gemini. 
    gemini = model.start_chat(history=[{
    'role': 'user',
    'parts': [
        {
            'text': json.dumps(pdf_content)
        },
        {
            #Código referente as orietações de como a IA deve se comportar ao analisar o PDF e instruções da estrutura do JSON.
            'text' : """"
            Você é minha assistente para a analise de documentos PDF. Todas as informações passadas são ficticias. Analise o documento passado e me retorne as informações no seguinte formato JSON:
                {
                 "contratada":"Retorne o nome da empresa contratada",
                 "cnpj_contratada":"Retorne o CNPJ da contratada",
                 "endereco_contratada":"Retorne o endereço da empresa contratada",
                 "contratante":"Retorne o nome da empresa contratante",
                 "cnpj_contratante":"Retorne o CNPJ da empresa contratante",
                 "endereco_contratante":"Retorne o endereço da empresa contratante",
                 "valor":"Retorne o valor do contrato",
                 "data_contrato":"Retorne a data",
                 "duracao_contrato":"Retorne a duração do contrato",
                 "pergunta_user":"Retorne a pergunta feita pelo user",
                 "resposta_gemini":"Retorne a resposta fornecida por você para a minha perfunta",
               }
               
                 Sempre retornar os dados descritos acima em formato json, independente de qual seja a pergunta feita pelo usuário.
                 Caso o PDF não seja um contrato, preencha o dicionário com 'null' nas posições de cadastro, com excessão dos campos de pergunta_user, resposta_gemini.
"""
            }
    ]
}])


    #Pergunta ao usuário o que o mesmo quer especificamente saber sobre o PDF. 
    message = input("Qual a sua pergunta sobre o PDF? ")

    #Envio da mensagem para a GEMINI e armazenamento da resposta na variável 'response'
    response = gemini.send_message(message)
    
    #Bloco de try exception com o objetivo de transformar a resposta da Gemini em um dict
    try:
        response_dict = response.to_dict()          #Tenta converter para um dicionário, se disponível
    except AttributeError:
        response_dict = str(response)

    #---------------------------------------------Configuração do MongoDB----------------------------------------------------
    #Conexão com banco de dados MongoDB
    cluster = MongoClient(MONGO_URI)
    db = cluster["desafio_lizardTI"]
    collection = db["desafio"]


    #Insere a respota completa da Gemini no banco de dados MongoDB.
    collection.insert_one({"resposta": response_dict})


    return response_dict                            #Retorne no formato adequado para FastAPI