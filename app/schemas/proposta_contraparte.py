from pydantic import BaseModel
from typing import List
from datetime import datetime

class PropostaContraparteBase(BaseModel):
    id_contraparte: int
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float
    

class PropostaContraparteCreate(BaseModel):
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float



class PropostaContraparteInDB(PropostaContraparteBase):
    id: int
    id_cliente: int


class PropostaContraparte(PropostaContraparteInDB):
    pass


class PropostaContraparteUpdate(BaseModel):
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float

class PropostaContraparteUpdateStatus(BaseModel):
    status: int