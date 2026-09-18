import pandas as pd
from config import api_key
import requests

#funcao para tabela de pontos corridos
# BL1  | Bundesliga
# DED  | Eredivisie
# BSA  | Campeonato Brasileiro Série A
# PD   | Primera Division
# FL1  | Ligue 1
# ELC  | Championship
# PPL  | Primeira Liga
# SA   | Serie A
# PL   | Premier League

def tabela_pontos_corridos(sigla_campeonato):
        
    url = f"https://api.football-data.org/v4/competitions/{sigla_campeonato}/standings"

    headers = {
        "X-Auth-Token": api_key
    }


    resposta = requests.get(url,headers=headers)

    dados = resposta.json()


    tabela = dados["standings"][0]["table"]

    dados_times=[]

    for time in tabela:
            dados_times.append({
            "posicao": time["position"],
            "time": time["team"]["name"],
            "jogos": time["playedGames"],
            "vitorias": time["won"],
            "empates": time["draw"],
            "derrotas": time["lost"],
            "pontos": time["points"],
            "gols_pro": time["goalsFor"],
            "gols_contra": time["goalsAgainst"],
            "saldo_gols": time["goalDifference"]
        })


    df  = pd. DataFrame(dados_times)

    df.to_csv(f'{sigla_campeonato}2026.csv', index=False, encoding='utf-8-sig') 
    #enconding para ajudar o BI a reconhecer corretamente caracteres como ã, ç, é.


def pegar_partidas (sigla_campeonato):
    url = f"https://api.football-data.org/v4/competitions/{sigla_campeonato}/matches"

    headers = {
        "X-Auth-Token": api_key
    }

    resposta = requests.get(url, headers=headers)

    dados = resposta.json()

    partidas = dados["matches"]
    dados_partidas = []
    for partida in partidas:
        dados_partidas.append({
            "data": partida["utcDate"],
            "rodada": partida["matchday"],
            "mandante": partida["homeTeam"]["name"],
            "visitante": partida["awayTeam"]["name"],
            "gols_mandante": partida["score"]["fullTime"]["home"],
            "gols_visitante": partida["score"]["fullTime"]["away"],
            "status": partida["status"]})

    df  = pd.DataFrame(dados_partidas)
    df["data"] = pd.to_datetime(df["data"])
    df.to_csv(f'todas_partidas_{sigla_campeonato}_2026.csv', index=False, encoding='utf-8-sig') 
    partidas_finalizadas = df[df["status"] == "FINISHED"].copy()
    partidas_finalizadas["data"] = pd.to_datetime(partidas_finalizadas["data"])
    partidas_finalizadas["gols_mandante"] = partidas_finalizadas["gols_mandante"].astype(int)
    partidas_finalizadas["gols_visitante"] = partidas_finalizadas["gols_visitante"].astype(int)
  
    partidas_finalizadas.to_csv(f'partidas_finalizadas_{sigla_campeonato}_2026.csv', index=False, encoding='utf-8-sig')


