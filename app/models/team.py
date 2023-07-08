from sqlalchemy import Column, Boolean, Integer, String, Float

from database import Base


class TeamEndOfSeason(Base):
    __tablename__ = "end_of_season"
    __table_args__ = {"schema": "team"}
    
    season        = Column(Integer, primary_key=True)
    lg            = Column(String, nullable=True)
    type          = Column(String, primary_key=True)
    number_tm     = Column(String, nullable=True)
    player        = Column(String, primary_key=True)
    position      = Column(String, nullable=True)
    seas_id       = Column(Integer, nullable=True)
    player_id     = Column(Integer, nullable=True)
    birth_year    = Column(Integer, nullable=True)
    tm            = Column(String, nullable=True)
    age           = Column(Integer, nullable=True)


class TeamSummary(Base):
    __tablename__ = "summaries"
    __table_args__ = {"schema": "team"}

    season            = Column(Integer, primary_key=True)
    lg                = Column(String, nullable=True)
    team              = Column(String, primary_key=True)
    abbreviation      = Column(String, nullable=True)
    playoffs          = Column(Boolean, nullable=True)
    age               = Column(Float, nullable=True)
    w                 = Column(Integer, nullable=True)
    l                 = Column(Integer, nullable=True)
    pw                = Column(Integer, nullable=True)
    pl                = Column(Integer, nullable=True)
    mov               = Column(Float, nullable=True)
    sos               = Column(Float, nullable=True)
    srs               = Column(Float, nullable=True)
    o_rtg             = Column(Float, nullable=True)
    d_rtg             = Column(Float, nullable=True)
    n_rtg             = Column(Float, nullable=True)
    pace              = Column(Float, nullable=True)
    f_tr              = Column(Float, nullable=True)
    x3p_ar            = Column(Float, nullable=True)
    ts_percent        = Column(Float, nullable=True)
    e_fg_percent      = Column(Float, nullable=True)
    tov_percent       = Column(Float, nullable=True)
    orb_percent       = Column(Float, nullable=True)
    ft_fga            = Column(Float, nullable=True)
    opp_e_fg_percent  = Column(Float, nullable=True)
    opp_tov_percent   = Column(Float, nullable=True)
    opp_drb_percent   = Column(Float, nullable=True)
    opp_ft_fga        = Column(Float, nullable=True)
    arena             = Column(String, nullable=True)
    attend            = Column(Integer, nullable=True)
    attend_g          = Column(Integer, nullable=True)


class TeamStatsPerGame(Base):
    __tablename__ = "stats_per_game"
    __table_args__ = {"schema": "team"}

    season         = Column(Integer, primary_key=True)
    lg             = Column(String, nullable=True)
    team           = Column(String, primary_key=True)
    abbreviation   = Column(String, nullable=True)
    playoffs       = Column(Boolean, nullable=True)
    g              = Column(Integer, nullable=True)
    mp_per_game    = Column(Float, nullable=True)
    fg_per_game    = Column(Float, nullable=True)
    fga_per_game   = Column(Float, nullable=True)
    fg_percent     = Column(Float, nullable=True)
    x3p_per_game   = Column(Float, nullable=True)
    x3pa_per_game  = Column(Float, nullable=True)
    x3p_percent    = Column(Float, nullable=True)
    x2p_per_game   = Column(Float, nullable=True)
    x2pa_per_game  = Column(Float, nullable=True)
    x2p_percent    = Column(Float, nullable=True)
    ft_per_game    = Column(Float, nullable=True)
    fta_per_game   = Column(Float, nullable=True)
    ft_percent     = Column(Float, nullable=True)
    orb_per_game   = Column(Float, nullable=True)
    drb_per_game   = Column(Float, nullable=True)
    trb_per_game   = Column(Float, nullable=True)
    ast_per_game   = Column(Float, nullable=True)
    stl_per_game   = Column(Float, nullable=True)
    blk_per_game   = Column(Float, nullable=True)
    tov_per_game   = Column(Float, nullable=True)
    pf_per_game    = Column(Float, nullable=True)
    pts_per_game   = Column(Float, nullable=True)


class TeamTotal(Base):
    __tablename__ = "totals"
    __table_args__ = {"schema": "team"}

    season         = Column(Integer, primary_key=True)
    lg             = Column(String, nullable=True)
    team           = Column(String, primary_key=True)
    abbreviation   = Column(String, nullable=True)
    playoffs       = Column(Boolean, nullable=True)
    g              = Column(Integer, nullable=True)
    mp             = Column(Integer, nullable=True)
    fg             = Column(Integer, nullable=True)
    fga            = Column(Integer, nullable=True)
    fg_percent     = Column(Float, nullable=True)
    x3p            = Column(Integer, nullable=True)
    x3pa           = Column(Integer, nullable=True)
    x3p_percent    = Column(Float, nullable=True)
    x2p            = Column(Integer, nullable=True)
    x2pa           = Column(Integer, nullable=True)
    x2p_percent    = Column(Float, nullable=True)
    ft             = Column(Integer, nullable=True)
    fta            = Column(Integer, nullable=True)
    ft_percent     = Column(Float, nullable=True)
    orb            = Column(Integer, nullable=True)
    drb            = Column(Integer, nullable=True)
    trb            = Column(Integer, nullable=True)
    ast            = Column(Integer, nullable=True)
    stl            = Column(Integer, nullable=True)
    blk            = Column(Integer, nullable=True)
    tov            = Column(Integer, nullable=True)
    pf             = Column(Integer, nullable=True)
    pts            = Column(Integer, nullable=True)