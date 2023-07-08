from sqlalchemy import Column, Boolean, Integer, String, Float

from database import Base


class PlayerCareer(Base):
    __tablename__ = "career_info"
    __table_args__ = {"schema": "player"}

    player_id     = Column(Integer, primary_key=True)
    player        = Column(String, nullable=True)
    birth_year    = Column(Integer, nullable=True)
    hof           = Column(Boolean, nullable=True)
    num_seasons   = Column(Integer, nullable=True)
    first_seas    = Column(Integer, nullable=True)
    last_seas     = Column(Integer, nullable=True)


class PlayerSeasonInfo(Base):
    __tablename__ = "season_info"
    __table_args__ = {"schema": "player"}

    season        = Column(Integer, nullable=True)
    seas_id       = Column(Integer, primary_key=True)
    player_id     = Column(Integer, primary_key=True)
    player        = Column(String, nullable=True)
    birth_year    = Column(Integer, nullable=True)
    pos           = Column(String, nullable=True)
    age           = Column(Integer, nullable=True)
    lg            = Column(String, nullable=True)
    tm            = Column(String, nullable=True)
    experience    = Column(Integer, nullable=True)


class PlayerStatsPerGame(Base):
    __tablename__ = "stats_per_game"
    __table_args__ = {"schema": "player"}

    seas_id        = Column(Integer, primary_key=True)
    season         = Column(Integer, nullable=True)
    player_id      = Column(Integer, primary_key=True)
    player         = Column(String, nullable=True)
    birth_year     = Column(Integer, nullable=True)
    pos            = Column(String, nullable=True)
    age            = Column(Integer, nullable=True)
    experience     = Column(Integer, nullable=True)
    lg             = Column(String, nullable=True)
    tm             = Column(String, nullable=True)
    g              = Column(Integer, nullable=True)
    gs             = Column(Integer, nullable=True)
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
    e_fg_percent   = Column(Float, nullable=True)
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


class PlayerTotal(Base):
    __tablename__ = "totals"
    __table_args__ = {"schema": "player"}

    seas_id        = Column(Integer, primary_key=True)
    season         = Column(Integer, nullable=True)
    player_id      = Column(Integer, primary_key=True)
    player         = Column(String, nullable=True)
    birth_year     = Column(Integer, nullable=True)
    pos            = Column(String, nullable=True)
    age            = Column(Integer, nullable=True)
    experience     = Column(Integer, nullable=True)
    lg             = Column(String, nullable=True)
    tm             = Column(String, nullable=True)
    g              = Column(Integer, nullable=True)
    gs             = Column(Integer, nullable=True)
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
    e_fg_percent   = Column(Float, nullable=True)
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