COPY team.end_of_season (season, lg, type, number_tm, player, position, seas_id, player_id, birth_year, tm, age)
FROM '/nba-stats/end-of-season-teams.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY team.summaries (season, lg, team, abbreviation, playoffs, age, w, l, pw, pl, mov, sos, srs, o_rtg, d_rtg, n_rtg, pace, f_tr, x3p_ar, ts_percent, e_fg_percent, tov_percent, orb_percent, ft_fga, opp_e_fg_percent, opp_tov_percent, opp_drb_percent, opp_ft_fga, arena, attend, attend_g)
FROM '/nba-stats/team-summaries.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY team.stats_per_game (season, lg, team, abbreviation, playoffs, g, mp_per_game, fg_per_game, fga_per_game, fg_percent, x3p_per_game, x3pa_per_game, x3p_percent, x2p_per_game, x2pa_per_game, x2p_percent, ft_per_game, fta_per_game, ft_percent, orb_per_game, drb_per_game, trb_per_game, ast_per_game, stl_per_game, blk_per_game, tov_per_game, pf_per_game, pts_per_game)
FROM '/nba-stats/team-stats-per-game.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY team.totals (season, lg, team, abbreviation, playoffs, g, mp, fg, fga, fg_percent, x3p, x3pa, x3p_percent, x2p, x2pa, x2p_percent, ft, fta, ft_percent, orb, drb, trb, ast, stl, blk, tov, pf, pts)
FROM '/nba-stats/team-totals.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY player.career_info (player_id, player, birth_year, hof, num_seasons, first_seas, last_seas)
FROM '/nba-stats/player-career-info.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY player.season_info (season, seas_id, player_id, player, birth_year, pos, age, lg, tm, experience)
FROM '/nba-stats/player-season-info.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY player.stats_per_game (seas_id, season, player_id, player, birth_year, pos, age, experience, lg, tm, g, gs, mp_per_game, fg_per_game, fga_per_game, fg_percent, x3p_per_game, x3pa_per_game, x3p_percent, x2p_per_game, x2pa_per_game, x2p_percent, e_fg_percent, ft_per_game, fta_per_game, ft_percent, orb_per_game, drb_per_game, trb_per_game, ast_per_game, stl_per_game, blk_per_game, tov_per_game, pf_per_game, pts_per_game)
FROM '/nba-stats/player-per-game.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;

COPY player.totals (seas_id, season, player_id, player, birth_year, pos, age, experience, lg, tm, g, gs, mp, fg, fga, fg_percent, x3p, x3pa, x3p_percent, x2p, x2pa, x2p_percent, e_fg_percent, ft, fta, ft_percent, orb, drb, trb, ast, stl, blk, tov, pf, pts)
FROM '/nba-stats/player-totals.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;