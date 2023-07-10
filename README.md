# Dockerizing a FastAPI app and a PostgreSQL database

Requisitos para rodar a aplicação: ter o Docker instalado.

[acesso aos arquivos](https://github.com/peuvitor/fastapi-docker)

## Overview

Criação de uma API em python utilizando o framework FastAPI que se conecta a um banco de dados PostgreSQL através do SQLAlchemy.

<img src="./images/diagram.png"/>

### Dataset

Disponível em: [NBA Stats (1947-present)](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)

Download: 14/jun/2023 (última modificação no site: 07/mai/2023)

[Glossário das estatísticas](https://www.basketball-reference.com/about/glossary.html)

### PostgreSQL database

A partir dos [arquivos .csv](https://github.com/peuvitor/fastapi-docker/tree/main/nba-stats) da base de dados utilizada, foram criadas e populadas os schemas e as tabelas. Isso se deu adicionando os [arquivos .sql](https://github.com/peuvitor/fastapi-docker/tree/main/sql-scripts) de DDL e DML no diretório `docker-entrypoint-initdb.d`, utilizado por padrão para rodar scripts na inicialização do container.

## Estrutura do projeto

```                                             
project
│   README.md                     #
│   docker-compose.yml            # configurações dos containers
│   openai.json                   # descrição da API criada
│                                 #
└───app                           #
│   │   __init__.py               #
│   │   main.py                   # arquivo principal da aplicação
│   │   database.py               # conexão com o banco de dados
│   │                             #
│   └───models                    # estrutura base para consulta ao banco de dados
│       │   __init__.py           #
│       │   player.py             #
│       │   team.py               #
│   └───routers                   # organizar endpoints e métodos
│       │   __init__.py           #
│       │   player.py             #
│       │   team.py               #
│   └───schemas                   # validar requisições e padronizar respostas
│       │   __init__.py           #
│       │   player.py             #
│       │   team.py               #
│                                 #
└───dockerfiles                   #
│   └───fastapi                   # criar imagem para a API
│       │   Dockerfile            #
│       │   requirements.txt      #
│                                 #
└───sql-scripts                   # criar e popular banco de dados
│   │   create_tables.sql         #
│   │   fill_tables.sql           #
│                                 #
└───nba-stats                     # dados escolhidos como base para o banco de dados
    │   end-of-season-teams.csv   #             
    │   player-career-info.csv    #
    │   player-per-game.csv       #
    │   player-season-info.csv    #
    │   player-totals.csv         #
    │   team-stats-per-game.csv   #
    │   team-summaries.csv        #
    │   team-totals.csv           #
│                                 #
└───images                        # imagens para o README.md
    │   *.png                     #      
```

## FastAPI app

- endpoints relacionados aos times:

    - `/teams/`: informação de um time de acordo com parâmetros de consulta 

    <img src="./images/01get_teams_params.PNG"/>

    - `/teams/{team_abb}`: informação de um time de acordo com parâmetros da rota

    <img src="./images/05get_teams_abb.PNG"/>

    - `/teams/`: criar um time de acordo com os dados passados no corpo da requisição

    <img src="./images/02post_add_team.PNG"/>

    - `/teams/{team_abb}/`: apagar um time de acordo com parâmetros da rota

    <img src="./images/06delete_teams.PNG"/>

    - `/teams/stats-per-game/`: estatísticas por jogo de um time

    <img src="./images/03get_teams_stats.PNG"/>

    - `/teams/totals/`: valores totais das estastísticas de um time

    <img src="./images/04get_teams_totals.PNG"/>

    - `/teams/season/{season}`: listar os times participantes de uma temporada

    <img src="./images/07get_teams_list.PNG"/>

    - `/teams/end-of-season/{season}/`: listar os times de final de temporada

    <img src="./images/08get_teams_end.PNG"/>


- endpoints relacionados aos jogadores:

    - `/players/`: participações de um jogador de acordo com os dados passados no corpo da requisição
    
    <img src="./images/01get_players_season.PNG"/>

    - `/players/all`: listar todos os jogadores
    
    <img src="./images/02get_players_all.PNG"/>

    - `/players/stats-per-game`: estatísticas por jogo de um jogador
    
    <img src="./images/03get_players_stats.PNG"/>

    - `/players/totals`: valores totais das estastísticas de um jogador
    
    <img src="./images/04get_players_totals.PNG"/>

    - `/players/{player_id}`: informação de um jogador de acordo com parâmetros da rota
    
    <img src="./images/05get_players_id.PNG"/>


## Exemplos de funcionamento