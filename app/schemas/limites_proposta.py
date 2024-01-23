from pydantic import BaseModel
from typing import List
class LimitesPropostaBase(BaseModel):
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_limite: int
    rating: int
    valor_limite: float
    valor_carteira: float
    carteira_mwm: float

class LimitesPropostaCreate(BaseModel):
    id_contraparte: int
    tipo_limite: int
    rating: int
    valor_limite: float
    valor_carteira: float
    carteira_mwm: float


class LimitesPropostaInDB(LimitesPropostaBase):
    id: int

    class Config:
        orm_mode = True

class LimitesProposta(LimitesPropostaInDB):
    pass

class LimitesPropostaUpdate(BaseModel):   
    tipo_limite: int
    rating: int
    valor_limite: float
    valor_carteira: float
    carteira_mwm: float