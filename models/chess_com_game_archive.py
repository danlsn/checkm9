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

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey, ARRAY, TIMESTAMP
from sqlalchemy.sql import func
import datetime
from base import Session, Base, engine
import requests
import requests_cache


class ChessComGameArchive(Base):
    __tablename__ = 'ChessComGameArchives'

    url = Column(String, primary_key=True)
    username = Column(String)
    date_month = Column(Date)
    games_count = Column(Integer)
    games = Column(ARRAY(String))
    last_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, archive_url):
        urls_expire_after = {
            f'''https://api.chess.com/pub/player/*/games/{datetime.datetime.now().strftime('%Y/%m/')}''': 0
        }
        req = requests_cache.CachedSession('cache/archive_url_cache',
                                           backend='filesystem',
                                           urls_expire_after=urls_expire_after)
        r = req.get(archive_url).json()
        parts = archive_url.split('/')
        username, archive_year, archive_month = parts[5], int(parts[7]), int(parts[8])
        games = r.get('games')
        self.username = username
        self.url = archive_url
        self.date_month = datetime.date(archive_year, archive_month, 1)
        self.games_count = len(games)
        self.games = [game.get('url') for game in games]
    pass


def main():
    archive_url = "https://api.chess.com/pub/player/danlsn/games/2020/12"
    archive = ChessComGameArchive("https://api.chess.com/pub/player/danlsn/games/2020/12")

    return


if __name__ == '__main__':
    main()
