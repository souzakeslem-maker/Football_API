import httpx
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://v3.football.api-sports.io"
API_KEY = os.getenv("FOOTBALL_API_KEY")

HEADERS = {
    "x-apisports-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

# Mapeamento de código de liga para ID numérico da API-Football
LIGAS = {
    "BSA": 71,   # Brasileirão Série A
    "PL": 39,    # Premier League
    "CL": 2,     # Champions League
    "BL1": 78,   # Bundesliga
    "SA": 135,   # Serie A (Itália)
    "FL1": 61,   # Ligue 1
    "LL": 140,   # La Liga
}

TEMPORADA = "2024"


def buscar_times_da_liga(codigo_liga: str) -> list:
    liga_id = LIGAS.get(codigo_liga.upper())

    if not liga_id:
        raise ValueError(f"Liga '{codigo_liga}' não suportada. Disponíveis: {list(LIGAS.keys())}")

    url = f"{BASE_URL}/teams"
    params = {"league": liga_id, "season": TEMPORADA}

    response = httpx.get(url, headers=HEADERS, params=params)

    print("STATUS:", response.status_code)       # <-- aqui
    print("RESPOSTA:", response.json())    


    response.raise_for_status()

    dados = response.json()
    times = dados.get("response", [])

    return [
        {
            "id": t["team"]["id"],
            "nome": t["team"]["name"],
            "sigla": t["team"]["code"],
            "escudo": t["team"]["logo"],
            "fundado": t["team"].get("founded"),
            "estadio": t["venue"].get("name"),
        }
        for t in times
    ]


def buscar_partidas_da_liga(codigo_liga: str, rodada: int = None) -> list:
    liga_id = LIGAS.get(codigo_liga.upper())

    if not liga_id:
        raise ValueError(f"Liga '{codigo_liga}' não suportada.")

    url = f"{BASE_URL}/fixtures"
    params = {"league": liga_id, "season": TEMPORADA}
    if rodada:
        params["round"] = f"Regular Season - {rodada}"

    response = httpx.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    dados = response.json()
    partidas = dados.get("response", [])

    return [
        {
            "id": p["fixture"]["id"],
            "rodada": p["league"]["round"],
            "data": p["fixture"]["date"],
            "status": p["fixture"]["status"]["long"],
            "time_casa": p["teams"]["home"]["name"],
            "time_fora": p["teams"]["away"]["name"],
            "placar_casa": p["goals"]["home"],
            "placar_fora": p["goals"]["away"],
        }
        for p in partidas
    ]


def buscar_artilheiros_da_liga(codigo_liga: str, limite: int = 10) -> list:
    liga_id = LIGAS.get(codigo_liga.upper())

    if not liga_id:
        raise ValueError(f"Liga '{codigo_liga}' não suportada.")

    url = f"{BASE_URL}/players/topscorers"
    params = {"league": liga_id, "season": TEMPORADA}

    response = httpx.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    dados = response.json()
    artilheiros = dados.get("response", [])

    return [
        {
            "posicao": index + 1,
            "jogador": a["player"]["name"],
            "time": a["statistics"][0]["team"]["name"],
            "gols": a["statistics"][0]["goals"]["total"],
            "assistencias": a["statistics"][0]["goals"].get("assists"),
        }
        for index, a in enumerate(artilheiros[:limite])
    ]