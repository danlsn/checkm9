"""
{
    "archives":[
        "https://api.chess.com/pub/player/danlsn/games/2020/12",
        "https://api.chess.com/pub/player/danlsn/games/2021/01",
        "https://api.chess.com/pub/player/danlsn/games/2021/02",
        "https://api.chess.com/pub/player/danlsn/games/2021/03",
        "https://api.chess.com/pub/player/danlsn/games/2021/04",
        "https://api.chess.com/pub/player/danlsn/games/2021/05",
        "https://api.chess.com/pub/player/danlsn/games/2021/06",
        "https://api.chess.com/pub/player/danlsn/games/2021/07",
        "https://api.chess.com/pub/player/danlsn/games/2021/08"
    ]
}
"""

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey
from base import Session, Base, engine


class ChessComGameArchive(Base):
    __tablename__ = 'ChessComGameArchives'

    id = Column(Integer, primary_key=True)
    dateMonth = Column(Date)
    url = Column(String)
    gamesCount = Column(Integer)
    games = ''
    pass


def main():
    return


if __name__ == '__main__':
    main()
