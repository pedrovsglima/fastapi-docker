CREATE SCHEMA team;
CREATE SCHEMA player;

CREATE TABLE team.end_of_season (
    season          INT               NOT NULL
    ,lg             VARCHAR(255)      NULL
    ,type           VARCHAR(255)      NOT NULL
    ,number_tm      VARCHAR(255)      NULL
    ,player         VARCHAR(255)      NOT NULL
    ,position       VARCHAR(255)      NULL
    ,seas_id        INT               NULL
    ,player_id      INT               NULL
    ,birth_year     INT               NULL
    ,tm             VARCHAR(255)      NULL
    ,age            INT               NULL
);

CREATE TABLE team.summaries (
    season             INT                  NOT NULL	
    ,lg                VARCHAR(255)         NULL
    ,team              VARCHAR(255)         NOT NULL
    ,abbreviation      VARCHAR(255)         NULL
    ,playoffs          BOOL                 NULL
    ,age               FLOAT                NULL
    ,w                 INT                  NULL
    ,l                 INT                  NULL
    ,pw                INT                  NULL
    ,pl                INT                  NULL
    ,mov               FLOAT                NULL
    ,sos               FLOAT                NULL
    ,srs               FLOAT                NULL
    ,o_rtg             FLOAT                NULL
    ,d_rtg             FLOAT                NULL
    ,n_rtg             FLOAT                NULL
    ,pace              FLOAT                NULL
    ,f_tr              FLOAT                NULL
    ,x3p_ar            FLOAT                NULL
    ,ts_percent        FLOAT                NULL
    ,e_fg_percent      FLOAT                NULL
    ,tov_percent       FLOAT                NULL
    ,orb_percent       FLOAT                NULL
    ,ft_fga            FLOAT                NULL
    ,opp_e_fg_percent  FLOAT                NULL
    ,opp_tov_percent   FLOAT                NULL
    ,opp_drb_percent   FLOAT                NULL
    ,opp_ft_fga        FLOAT                NULL
    ,arena             VARCHAR(255)         NULL
    ,attend            INT                  NULL	
    ,attend_g          INT                  NULL    
);

CREATE TABLE team.stats_per_game (
    season                 INT               NOT NULL	
    ,lg                    VARCHAR(255)      NULL	
    ,team                  VARCHAR(255)      NOT NULL	
    ,abbreviation          VARCHAR(255)      NULL	
    ,playoffs              BOOL              NULL	
    ,g                     INT               NULL	
    ,mp_per_game           FLOAT             NULL	
    ,fg_per_game           FLOAT             NULL	
    ,fga_per_game          FLOAT             NULL	
    ,fg_percent            FLOAT             NULL	
    ,x3p_per_game          FLOAT             NULL	
    ,x3pa_per_game         FLOAT             NULL	
    ,x3p_percent           FLOAT             NULL	
    ,x2p_per_game          FLOAT             NULL	
    ,x2pa_per_game         FLOAT             NULL	
    ,x2p_percent           FLOAT             NULL	
    ,ft_per_game           FLOAT             NULL	
    ,fta_per_game          FLOAT             NULL	
    ,ft_percent            FLOAT             NULL	
    ,orb_per_game          FLOAT             NULL	
    ,drb_per_game          FLOAT             NULL	
    ,trb_per_game          FLOAT             NULL	
    ,ast_per_game          FLOAT             NULL	
    ,stl_per_game          FLOAT             NULL	
    ,blk_per_game          FLOAT             NULL	
    ,tov_per_game          FLOAT             NULL	
    ,pf_per_game           FLOAT             NULL	
    ,pts_per_game          FLOAT             NULL
);

CREATE TABLE team.totals (
    season                 INT               NOT NULL	
    ,lg                    VARCHAR(255)      NULL	
    ,team                  VARCHAR(255)      NOT NULL	
    ,abbreviation          VARCHAR(255)      NULL	
    ,playoffs              BOOL              NULL	
    ,g                     INT               NULL
    ,mp                    INT               NULL	
    ,fg                    INT               NULL	
    ,fga                   INT               NULL	
    ,fg_percent            FLOAT             NULL	
    ,x3p                   INT               NULL	
    ,x3pa                  INT               NULL	
    ,x3p_percent           FLOAT             NULL	
    ,x2p                   INT               NULL	
    ,x2pa                  INT               NULL	
    ,x2p_percent           FLOAT             NULL	
    ,ft                    INT               NULL	
    ,fta                   INT               NULL	
    ,ft_percent            FLOAT             NULL	
    ,orb                   INT               NULL	
    ,drb                   INT               NULL	
    ,trb                   INT               NULL	
    ,ast                   INT               NULL	
    ,stl                   INT               NULL	
    ,blk                   INT               NULL	
    ,tov                   INT               NULL	
    ,pf                    INT               NULL	
    ,pts                   INT               NULL
);

CREATE TABLE player.career_info (
    player_id        INT            NOT NULL	
    ,player          VARCHAR(255)   NULL	
    ,birth_year      INT            NULL	
    ,hof             BOOL           NULL	
    ,num_seasons     INT            NULL	
    ,first_seas      INT            NULL	
    ,last_seas       INT            NULL
);

CREATE TABLE player.season_info (
    season          INT               NULL
    ,seas_id        INT               NOT NULL
    ,player_id      INT               NOT NULL
    ,player         VARCHAR(255)      NULL
    ,birth_year     INT               NULL
    ,pos            VARCHAR(255)      NULL
    ,age            INT               NULL
    ,lg             VARCHAR(255)      NULL
    ,tm             VARCHAR(255)      NULL
    ,experience     INT               NULL 
);

CREATE TABLE player.stats_per_game (
    seas_id               INT            NOT NULL	
    ,season               INT            NULL	
    ,player_id            INT            NOT NULL	
    ,player               VARCHAR(255)   NULL	
    ,birth_year           INT            NULL	
    ,pos                  VARCHAR(255)   NULL	
    ,age                  INT            NULL	
    ,experience           INT            NULL	
    ,lg                   VARCHAR(255)   NULL	
    ,tm                   VARCHAR(255)   NULL	
    ,g                    INT            NULL	
    ,gs                   INT            NULL	
    ,mp_per_game          FLOAT          NULL	
    ,fg_per_game          FLOAT          NULL	
    ,fga_per_game         FLOAT          NULL	
    ,fg_percent           FLOAT          NULL	
    ,x3p_per_game         FLOAT          NULL	
    ,x3pa_per_game        FLOAT          NULL	
    ,x3p_percent          FLOAT          NULL	
    ,x2p_per_game         FLOAT          NULL	
    ,x2pa_per_game        FLOAT          NULL	
    ,x2p_percent          FLOAT          NULL	
    ,e_fg_percent         FLOAT          NULL	
    ,ft_per_game          FLOAT          NULL	
    ,fta_per_game         FLOAT          NULL	
    ,ft_percent           FLOAT          NULL	
    ,orb_per_game         FLOAT          NULL	
    ,drb_per_game         FLOAT          NULL	
    ,trb_per_game         FLOAT          NULL	
    ,ast_per_game         FLOAT          NULL	
    ,stl_per_game         FLOAT          NULL	
    ,blk_per_game         FLOAT          NULL	
    ,tov_per_game         FLOAT          NULL	
    ,pf_per_game          FLOAT          NULL	
    ,pts_per_game         FLOAT          NULL
);

CREATE TABLE player.totals (
    seas_id             INT                 NOT NULL	
    ,season             INT                 NULL	
    ,player_id          INT                 NOT NULL	
    ,player             VARCHAR(255)        NULL	
    ,birth_year         INT                 NULL	
    ,pos                VARCHAR(255)        NULL	
    ,age                INT                 NULL	
    ,experience         INT                 NULL	
    ,lg                 VARCHAR(255)        NULL	
    ,tm                 VARCHAR(255)        NULL	
    ,g                  INT                 NULL	
    ,gs                 INT                 NULL	
    ,mp                 INT                 NULL	
    ,fg                 INT                 NULL	
    ,fga                INT                 NULL	
    ,fg_percent         FLOAT               NULL	
    ,x3p                INT                 NULL	
    ,x3pa               INT                 NULL	
    ,x3p_percent        FLOAT               NULL	
    ,x2p                INT                 NULL	
    ,x2pa               INT                 NULL	
    ,x2p_percent        FLOAT               NULL	
    ,e_fg_percent       FLOAT               NULL	
    ,ft                 INT                 NULL	
    ,fta                INT                 NULL	
    ,ft_percent         FLOAT               NULL	
    ,orb                INT                 NULL	
    ,drb                INT                 NULL	
    ,trb                INT                 NULL	
    ,ast                INT                 NULL	
    ,stl                INT                 NULL	
    ,blk                INT                 NULL	
    ,tov                INT                 NULL	
    ,pf                 INT                 NULL	
    ,pts                INT                 NULL
);