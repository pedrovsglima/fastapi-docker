COPY team.summaries (season, lg, team, abbreviation, playoffs, age, w, l, pw, pl, mov, sos, srs, o_rtg, d_rtg, n_rtg, pace, f_tr, x3p_ar, ts_percent, e_fg_percent, tov_percent, orb_percent, ft_fga, opp_e_fg_percent, opp_tov_percent, opp_drb_percent, opp_ft_fga, arena, attend, attend_g)
FROM '/nba-stats/team-summaries.csv'
DELIMITER ','
NULL AS 'NA'
CSV HEADER;