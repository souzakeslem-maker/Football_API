from fastapi import APIRouter, HTTPException
from football_app import buscar_times_da_liga

times_router = APIRouter(prefix="/times", tags=["Times"])

@times_router.get('/{codigo_liga}')
def listar_times(codigo_liga: str):
    '''
    retona todos os times de uma liga.

    exemplos:
    - GET/ BSA - Brasileirao
    - GET/ PL - Premier league
    '''
    try:
        times = buscar_times_da_liga(codigo_liga.upper())
        return {'liga': codigo_liga.upper(), "total": len(times), "times": times}
        print("RESPOSTA COMPLETA:", response.json()) 
    except Exception as e:
        print(f"ERRO: {e}")  # vai aparecer no terminal do uvicorn
        raise HTTPException(status_code=400, detail=str(e))
    