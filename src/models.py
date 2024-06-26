from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Union


class Orgao(str, Enum):
    tipo_1 = 'TODOS OS ÓRGÃOS OU ENTIDADES'
    tipo_2 = 'AGENCIA DE DESENVOLVIMENTO DA ECONOMIA DO MAR DE FORTALEZA'
    tipo_3 = 'AGENCIA DE FISCALIZACAO DE FORTALEZA'
    tipo_4 = 'AGENCIA DE REGULACAO, FISCALIZACAO E CONTROLE DOS SERVICOS PUBLICOS DE SANEAMENTO AMBIENTAL'
    tipo_5 = 'AUTARQUIA DE URBANISMO E PAISAGISMO DE FORTALEZA'
    tipo_6 = 'AUTARQUIA MUNICIPAL DE TRANSITO E CIDADANIA'
    tipo_7 = 'CAMARA MUNICIPAL DE FORTALEZA'
    tipo_8 = 'CENTRAL DE LICITACOES DA PREFEITURA DE FORTALEZA'
    tipo_9 = 'COMPANHIA DE TRANSPORTE COLETIVO - CTC'
    tipo_10 = 'CONTROLADORIA E OUVIDORIA GERAL DO MUNICIPIO'
    tipo_11 = 'COORDENADORIA ESPECIAL DE PROTECAO E BEM-ESTAR ANIMAL'
    tipo_12 = 'DEPARTAMENTO MUNICIPAL DE PROTECAO E DEFESA DOS DIREITOS DO CONSUMIDOR'
    tipo_13 = 'EMPRESA DE TRANSPORTE URBANO DE FORTALEZA'
    tipo_14 = 'FRIGORÍFICO INDUSTRIAL DE FORTALEZA S.A'
    tipo_15 = 'FUNDACAO DA CRIANCA E DA FAMILIA CIDADA'
    tipo_16 = 'FUNDACAO DE CIENCIA, TECNOLOGIA E INOVACAO DE FORTALEZA'
    tipo_17 = 'FUNDO DE APERFEICOAMENTO DA PROCURADORIA GERAL DO MUNICIPIO'
    tipo_18 = 'FUNDO DE DEFESA DO MEIO AMBIENTE'
    tipo_19 = 'FUNDO DE INVESTIMENTO E DESENVOLVIMENTO DE ATIVIDADES DA ADMINISTRACAO FAZENDARIA'
    tipo_20 = 'FUNDO ESPECIAL DA CAMARA MUNICIPAL DE FORTALEZA'
    tipo_21 = 'FUNDO MUNICIPAL DE ASSISTENCIA SOCIAL'
    tipo_22 = 'FUNDO MUNICIPAL DE CULTURA'
    tipo_23 = 'FUNDO MUNICIPAL DE DEFESA DOS DIREITOS DA CRIANCA E DO ADOLESCENTE'
    tipo_24 = 'FUNDO MUNICIPAL DE DEFESA DOS DIREITOS DIFUSOS'
    tipo_25 = 'FUNDO MUNICIPAL DE DESENVOLVIMENTO ECONOMICO'
    tipo_26 = 'FUNDO MUNICIPAL DE DESENVOLVIMENTO URBANO'
    tipo_27 = 'FUNDO MUNICIPAL DE EDUCACAO'
    tipo_28 = 'FUNDO MUNICIPAL DE EDUCACAO ? INFRAESTRUTURA'
    tipo_29 = 'FUNDO MUNICIPAL DE HABITACAO DE INTERESSE SOCIAL'
    tipo_30 = 'FUNDO MUNICIPAL DE JUVENTUDE DE FORTALEZA'
    tipo_31 = 'FUNDO MUNICIPAL DE LIMPEZA URBANA'
    tipo_32 = 'FUNDO MUNICIPAL DE POLITICAS SOBRE DROGAS'
    tipo_33 = 'FUNDO MUNICIPAL DE SAUDE'
    tipo_34 = 'FUNDO MUNICIPAL DE SAUDE - INFRAESTRUTURA'
    tipo_35 = 'FUNDO MUNICIPAL DE SEGURANCA CIDADA'
    tipo_36 = 'FUNDO MUNICIPAL DOS DIREITOS HUMANOS DA PESSOA IDOSA'
    tipo_37 = 'FUNDO MUNICIPAL PARA PROTECAO DOS DIREITOS DA PESSOA COM DEFICIENCIA'
    tipo_38 = 'FUNDO PREVIDENCIARIO PREVIFOR/PRE'
    tipo_39 = 'GABINETE DO PREFEITO'
    tipo_40 = 'GABINETE DO VICE-PREFEITO'
    tipo_41 = 'GUARDA MUNICIPAL DE FORTALEZA'
    tipo_42 = 'HOSPITAL DISTRITAL MARIA JOSE BARROSO DE OLIVEIRA'
    tipo_43 = 'HOSPITAL DISTRITAL EDMILSON BARROS DE OLIVEIRA'
    tipo_44 = 'HOSPITAL DISTRITAL EVANDRO AYRES DE MOURA'
    tipo_45 = 'HOSPITAL DISTRITAL GONZAGA MOTA/BARRA DO CEARA'
    tipo_46 = 'HOSPITAL DISTRITAL GONZAGA MOTA/JOSE WALTER'
    tipo_47 = 'HOSPITAL DISTRITAL GONZAGA MOTA/MESSEJANA'
    tipo_48 = 'HOSPITAL E MATERNIDADE DRA ZILDA ARNS NEUMANN'
    tipo_49 = 'INSTITUTO DE PLANEJAMENTO DE FORTALEZA'
    tipo_50 = 'INSTITUTO DE PREVIDENCIA DO MUNICIPIO - ASSISTENCIA A SAUDE DOS SERVIDORES DO MUNICIPIO DE FORTALEZA'
    tipo_51 = 'INSTITUTO DE PREVIDENCIA DO MUNICIPIO - PREVFOR'
    tipo_52 = 'INSTITUTO DR. JOSE FROTA'
    tipo_53 = 'INSTITUTO MUNICIPAL DE DESENVOLVIMENTO DE RECURSOS HUMANOS'
    tipo_54 = 'PROCURADORIA GERAL DO MUNICIPIO'
    tipo_55 = 'RECURSOS SOB A SUPERVISAO DA SECRETARIA MUNICIPAL DAS FINANCAS'
    tipo_56 = 'RECURSOS SOB A SUPERVISAO DA SECRETARIA MUNICIPAL DO PLANEJAMENTO, ORCAMENTO E GESTAO'
    tipo_57 = 'RESERVA DE CONTINGENCIA'
    tipo_58 = 'SECRETARIA MUNICIPAL DA CONSERVACAO E SERVICOS PUBLICOS'
    tipo_59 = 'SECRETARIA MUNICIPAL DA CULTURA DE FORTALEZA'
    tipo_60 = 'SECRETARIA MUNICIPAL DA EDUCACAO'
    tipo_61 = 'SECRETARIA MUNICIPAL DA GESTAO REGIONAL'
    tipo_62 = 'SECRETARIA MUNICIPAL DA INFRAESTRUTURA'
    tipo_63 = 'SECRETARIA MUNICIPAL DA JUVENTUDE'
    tipo_64 = 'SECRETARIA MUNICIPAL DA SAUDE'
    tipo_65 = 'SECRETARIA MUNICIPAL DA SEGURANCA CIDADA'
    tipo_66 = 'SECRETARIA MUNICIPAL DAS FINANCAS'
    tipo_67 = 'SECRETARIA MUNICIPAL DE GOVERNO'
    tipo_68 = 'SECRETARIA MUNICIPAL DO DESENVOLVIMENTO HABITACIONAL DE FORTALEZA'
    tipo_69 = 'SECRETARIA MUNICIPAL DO ESPORTE E LAZER'
    tipo_70 = 'SECRETARIA MUNICIPAL DO PLANEJAMENTO, ORCAMENTO E GESTAO'
    tipo_71 = 'SECRETARIA MUNICIPAL DO TURISMO DE FORTALEZA'
    tipo_72 = 'SECRETARIA MUNICIPAL DO URBANISMO E MEIO AMBIENTE'
    tipo_73 = 'SECRETARIA MUNICIPAL DOS DIREITOS HUMANOS E DESENVOLVIMENTO SOCIAL'
   


class ResponseSite(BaseModel):
    ORGAO: str = ''
    DATAINICIO: str = ''
    DATAFIM: str = ''
    FONTE_PESQUISA: Optional[Union[int, str]]  = 'Portal da transparência Fortaleza'
    ID: Optional[Union[int, str]]  = ''
    IDPARCELA: Optional[Union[int, str]]  = ''
    IDEMPENHO: Optional[Union[int, str]]  = ''
    EXERCICIO: Optional[Union[int, str]]  = ''
    CODIGOCOMPLETOUO: Optional[Union[int, str]]  = ''
    CODIGOORGAO: Optional[Union[int, str]]  = ''
    CODIGOUNIDADE: Optional[Union[int, str]]  = ''
    DESCRICAOUO: Optional[Union[int, str]]  = ''
    SIGLAUO: Optional[Union[int, str]]  = ''
    ORGAOREDUZIDO: Optional[Union[int, str]]  = ''
    NUMEROEMPENHO: Optional[Union[int, str]]  = ''
    PARCELAEMPENHO: Optional[Union[int, str]]  = ''
    DATAEMPENHO: Optional[Union[int, str]]  = ''
    DATALIQUIDACAO: Optional[Union[int, str]]  = ''
    DATAPAGAMENTO: Optional[Union[int, str]]  = ''
    FASE: Optional[Union[int, str]] = ''
    ESPECIEEMPENHO: Optional[Union[int, str]]  = ''
    RESTOSAPAGAR: Optional[float] = ''
    OBJETOEMPENHO: Optional[Union[int, str]]  = ''
    IDCREDOR: int = '' 
    DOCUMENTOCREDOR: Optional[Union[int, str]]  = ''
    NOMECREDOR: Optional[Union[int, str]]  = ''
    CODIGODOTACAO: Optional[Union[int, str]]  = ''
    CODIGOFUNCAO: Optional[Union[int, str]]  = ''
    DESCRICAOOFUNCAO: Optional[Union[int, str]]  = ''
    CODIGOSUBFUNCAO: Optional[Union[int, str]]  = ''
    DESCRICAOSUBFUNCAO: Optional[Union[int, str]]  = ''
    CODIGOPROGRAMA: Optional[Union[int, str]]  = ''
    DESCRICAOPROGRAMA: Optional[Union[int, str]]  = ''
    CODIGOATIVIDADE: Optional[Union[int, str]]  = ''
    DESCRICAOATIVIDADE: Optional[Union[int, str]]  = ''
    CODIGOSUBATIVIDADE: Optional[Union[int, str]]  = ''
    CATEGORIAECONOMICA: Optional[Union[int, str]]  = ''
    DESCRICAOCATEGORIAECONOMICA: Optional[Union[int, str]]  = ''
    GRUPONATUREZA: Optional[Union[int, str]]  = ''
    DESCRICAOGRUPONATUREZA: Optional[Union[int, str]]  = ''
    MODALIDADEAPLICACAO: Optional[Union[int, str]]  = ''
    DESCRICAOMODALIDADEAPLICACAO: Optional[Union[int, str]]  = ''
    CODIGOELEMENTO: Optional[Union[int, str]]  = ''
    DESCRICAOELEMENTO: Optional[Union[int, str]]  = ''
    INDICADORUSO: Optional[Union[int, str]]  = ''
    CODIGOFONTE: Optional[Union[int, str]]  = ''
    DESCRICAOFONTE: Optional[Union[int, str]]  = ''
    SUBELEMENTOS: Optional[Union[int, str]]  = ''
    IDLICITACAO: Optional[Union[int, str]] = ''
    EXERCICIOLICITACAO: Optional[Union[int, str]] = ''
    NUMEROLICITACAO: Optional[Union[int, str]] = ''
    CODIGOMODALIDADEPROCESSO: Optional[Union[int, str]] = ''
    DESCRICAOMODALIDADEPROCESSO: Optional[Union[int, str]] = ''
    CODIGOMODALIDADELICITACAO: Optional[Union[int, str]] = ''
    DESCRICAOMODALIDADELICITACAO: Optional[Union[int, str]] = ''
    VALOREMPENHADO: Optional[Union[float, int]] = ''
    VALORPARCELA: Optional[Union[float, int]] = ''
    VALORLIQUIDADO: Optional[Union[float, int]] = ''
    VALORPAGO: Optional[Union[float, int]] = ''
    VALORRETENCOES: Optional[Union[float, int]] = ''
    VALORANULADO: Optional[Union[float, int]] = ''

class ResponseDefault(BaseModel):
    code: int
    message: str
    datetime: str
    results: List[ResponseSite]

class ResponseError(BaseModel):
    code: int
    message: str