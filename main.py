from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from times import times_router
from partidas import partidas_router
from artilheiros import artilheiros_router



# Cria a aplicação FastAPI
app = FastAPI(
    title="Futebol API",
    description="API de estatísticas de futebol consumindo dados da football-data.org",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # endereço do React
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas (cada arquivo de routes é um "pedaço" da API)
app.include_router(times_router)
app.include_router(partidas_router)
app.include_router(artilheiros_router)

@app.get("/")
def root():
    return {"message": "Futebol API rodando! Acesse /docs para ver os endpoints."}

