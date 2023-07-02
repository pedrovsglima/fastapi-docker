CREATE SCHEMA team;

DROP TABLE IF EXISTS team.summaries;
CREATE TABLE team.summaries (
    season            int                   NULL	
    ,lg                varchar(255)         NULL
    ,team              varchar(255)         NULL
    ,abbreviation      varchar(255)         NULL
    ,playoffs          bool                 NULL
    ,age               float                NULL
    ,w                 int                  NULL
    ,l                 int                  NULL
    ,pw                int                  NULL
    ,pl                int                  NULL
    ,mov               float                NULL
    ,sos               float                NULL
    ,srs               float                NULL
    ,o_rtg             float                NULL
    ,d_rtg             float                NULL
    ,n_rtg             float                NULL
    ,pace              float                NULL
    ,f_tr              float                NULL
    ,x3p_ar            float                NULL
    ,ts_percent        float                NULL
    ,e_fg_percent      float                NULL
    ,tov_percent       float                NULL
    ,orb_percent       float                NULL
    ,ft_fga            float                NULL
    ,opp_e_fg_percent  float                NULL
    ,opp_tov_percent   float                NULL
    ,opp_drb_percent   float                NULL
    ,opp_ft_fga        float                NULL
    ,arena             varchar(255)         NULL
    ,attend            int                  NULL	
    ,attend_g          int                  NULL    
);