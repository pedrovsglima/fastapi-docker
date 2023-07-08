# Dockerizing FastAPI 

Base de dados: [NBA Stats (1947-present)](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)

Download: 14/jun/2023

Última modificação no site: 07/mai/2023

[Glossário das estatísticas](https://www.basketball-reference.com/about/glossary.html)

## Dataset

- end of season:

    - end-of-season-teams: season, player (name, age, team, position), type (All-Defense, All-NBA, All-Rookie)

- players:

    - player-career-info: player_id, name, hall of fame, num seasons, first season, last season

    - player-season-info: season, seas_id, player_id, player (id, position, age, years of experience), team

    - player-per-game: season, player (id, name, age, position, years of experience, team), stats

    - player-totals: season, player (id, name, age, position, years of experience, team), totals (points, blocks, etc)

- teams:

    - team-summaries: season, team, playoff (boolean), stats about season

    - team-stats-per-game (teams and league average): season, team, playoff (boolean), stats per game (points, defense, etc)

    - team-totals: season, team, playoff (boolean), totals (points, blocks, etc)