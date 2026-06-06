from fastapi import APIRouter, HTTPException
from football_app import buscar_partidas_da_liga

partidas_router = APIRouter(prefix="/partidas", tags=["Partidas"])

@partidas_router.get("/{codigo_liga}")
def listar_times(codigo_liga: str):
    """
    Retorna todos os times de uma liga.
    
    Exemplos:
    - GET /times/BSA  → Brasileirão
    - GET /times/PL   → Premier League
    """
    try:
        partidas = buscar_partidas_da_liga(codigo_liga.upper())
        return {"liga": codigo_liga.upper(), "total": len(partidas), "partidas": partidas}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
