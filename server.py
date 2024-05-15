# stdlib imports
import logging
import time
from os import environ as env

# 3rd party imports
from fastapi.logger import logger as fastapi_logger
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from src import models, consulta

# Define configuracoes basicas para o logger
msg_frt = "[%(asctime)s] %(levelname)s [%(name)s] - %(message)s"
time_frt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(msg_frt, time_frt)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
LOG_LEVEL = env.get('LOG_LEVEL', default='INFO')
fastapi_logger.addHandler(handler)
fastapi_logger.setLevel(LOG_LEVEL)

logger_name = env.get('BOT_NAME', default='informacoes-de-convenios')
fastapi_logger.name = logger_name

desc = '<a href="https://portaltransparencia.fortaleza.ce.gov.br/#/despesas/detalhadas" target="_blank">FONTE</a>'

tags_metadata = [
    {
        'name': 'despesas-transparencia-fortaleza',
        'description': 'Consulta Portal Tranparencia Fortaleza - despesas detalhadas'
    }
]

responses = {
    407: {'model': models.ResponseError, 'description': 'Proxy Authentication Required'},
    422: {'model': models.ResponseError, 'description': 'Unprocessable Entity'},
    500: {'model': models.ResponseError, 'description': 'Erro interno no servidor'},
    502: {'model': models.ResponseError, 'description': 'Bad Gateway'},
    504: {'model': models.ResponseError, 'description': 'Conexao com o site excedeu tempo limite'},
    509: {'model': models.ResponseError, 'description': 'Nao foi possivel resolver o captcha'},
    512: {'model': models.ResponseError, 'description': 'Erro ao executar parse da pagina'},
    513: {'model': models.ResponseError, 'description': 'Argumentos invalidos'}

}

#---------------------------- Application -------------------------------
app = FastAPI(
    title='REST API - Consulta Portal Transparência Fortaleza - despesas detalhadas', 
    description=desc, 
    debug=False, 
    openapi_tags=tags_metadata,
    openapi_url="/api/despesas-transparencia-fortaleza/consulta/docs/openapi.json",
    docs_url='/api/despesas-transparencia-fortaleza/consulta/docs'
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

#---------------------------- Query params -------------------------------
data_inicio = Query(
     ..., 
    description='Data de cadastro no formato: DD/MM/AAAA',
    regex='\d{2}/\d{2}/\d{4}'
)

data_fim = Query(
     ..., 
    description='Data de cadastro no formato: DD/MM/AAAA',
    regex='\d{2}/\d{2}/\d{4}'
)
#---------------------------- Endpoints -------------------------------
@app.get(
    path=f"/api/despesas-transparencia-fortaleza/consulta", 
    tags=['despesas-transparencia-fortaleza'],
    responses=responses)
async def get_consulta(data_inicio: str = data_inicio, 
                       data_fim: str = data_fim,
                       orgao: models.Orgao = None):    
    return await consulta.fetch( data_inicio, data_fim, orgao)


#--------------------------- Static Files ------------------------------
app.mount("/", StaticFiles(directory="static", html=True), name="static")