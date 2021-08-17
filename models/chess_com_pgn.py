from sqlalchemy import Column, String, Integer, Date, DateTime, Time, Boolean, ForeignKey
from base import Session, Base, engine


class ChessComGamePgn(Base):
    __tablename__ = 'ChessComGamePgns'

    id = Column(Integer, primary_key=True)
    pgn = Column(String)
    site = Column(String)
    event = Column(String)
    date = Column(Date)
    round = Column(String)
    white = Column(String)
    black = Column(String)
    result = Column(String)
    current_position = Column(String)
    timezone = Column(String)
    eco = Column(String)
    eco_url = Column(String)
    utc_date = Column(Date)
    utc_time = Column(Time)
    white_elo = Column(Integer)
    black_elo = Column(Integer)
    time_control = Column(String)
    termination = Column(String)
    start_time = Column(Time)
    end_date = Column(Date)
    end_time = Column(Time)
    link = Column(String)
    moves = Column(String)


def main():
    return


if __name__ == '__main__':
    main()
