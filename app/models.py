from sqlalchemy import Column, Boolean, Integer, String, Float

from database import Base

class TeamSummary(Base):
    __tablename__ = "summaries"
    __table_args__ = {"schema": "team"}

    season = Column(Integer, primary_key=True)
    lg = Column(String, nullable=True)
    team = Column(String, nullable=True)
    abbreviation = Column(String, primary_key=True)
    playoffs = Column(Boolean, nullable=True)
    age = Column(Float, nullable=True)
    w = Column(Integer, nullable=True)
    l = Column(Integer, nullable=True)
    pw = Column(Integer, nullable=True)
    pl = Column(Integer, nullable=True)
    mov = Column(Float, nullable=True)
    sos = Column(Float, nullable=True)
    srs = Column(Float, nullable=True)
    o_rtg = Column(Float, nullable=True)
    d_rtg = Column(Float, nullable=True)
    n_rtg = Column(Float, nullable=True)
    pace = Column(Float, nullable=True)
    f_tr = Column(Float, nullable=True)
    x3p_ar = Column(Float, nullable=True)
    ts_percent = Column(Float, nullable=True)
    e_fg_percent = Column(Float, nullable=True)
    tov_percent = Column(Float, nullable=True)
    orb_percent = Column(Float, nullable=True)
    ft_fga = Column(Float, nullable=True)
    opp_e_fg_percent = Column(Float, nullable=True)
    opp_tov_percent = Column(Float, nullable=True)
    opp_drb_percent = Column(Float, nullable=True)
    opp_ft_fga = Column(Float, nullable=True)
    arena = Column(String, nullable=True)
    attend = Column(Integer, nullable=True)
    attend_g = Column(Integer, nullable=True)