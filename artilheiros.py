from fastapi import APIRouter, HTTPException
from football_app import buscar_artilheiros_da_liga

artilheiros_router = APIRouter(prefix="/artilheiros", tags=["Artilheiros"])

@artilheiros_router.get("/{codigo_liga}")
def listar_artilheiros(codigo_liga: str, limite: int = 10):
    """
    Retorna os artilheiros de uma liga.
    Parâmetro opcional: ?limite=5
    
    Exemplos:
    - GET /artilheiros/BSA          → top 10
    - GET /artilheiros/PL?limite=5  → top 5 da Premier League
    """
    try:
        artilheiros = buscar_artilheiros_da_liga(codigo_liga.upper(), limite)
        return {"liga": codigo_liga.upper(), "artilheiros": artilheiros}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
