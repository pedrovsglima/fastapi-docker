# Dockerizing a FastAPI app and a PostgreSQL database

Requisitos para rodar a aplicação: ter o Docker instalado.

[acesso aos arquivos](https://github.com/peuvitor/fastapi-docker)

## Overview

Criação de uma API em python utilizando o framework FastAPI que se conecta a um banco de dados PostgreSQL através do SQLAlchemy.

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
```

## FastAPI app



## Exemplos de funcionamento