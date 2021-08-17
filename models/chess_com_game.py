"""
{
    "url": "https://www.chess.com/game/live/6331932939",
    "pgn": <pgn string>
    "time_control": "300",
    "end_time": 1611497538,
    "rated": true,
    "fen": "<fen string>",
    "time_class": "blitz",
    "rules": "chess",
    "white": {
      "rating": 579,
      "result": "win",
      "@id": "https://api.chess.com/pub/player/jickhon",
      "username": "jickhon"
    },
    "black": {
      "rating": 494,
      "result": "checkmated",
      "@id": "https://api.chess.com/pub/player/danlsn",
      "username": "danlsn"
    }
  },

  Game results codes

In the table below are listed all codes that are returned by game related endpoints.

*Code*	                *Description*
______________________________________________________________
win	                    Win
checkmated	            Checkmated
agreed	                Draw agreed
repetition	            Draw by repetition
timeout	                Timeout
resigned	            Resigned
stalemate	            Stalemate
lose	                Lose
insufficient	        Insufficient material
50move	                Draw by 50-move rule
abandoned	            Abandoned
kingofthehill	        Opponent king reached the hill
threecheck	            Checked for the 3rd time
timevsinsufficient	    Draw by timeout vs insufficient material
bughousepartnerlose	    Bughouse partner lost
______________________________________________________________

"""
from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey, BigInteger
import datetime
from base import Session, Base, engine


class ChessComGame(Base):
    __tablename__ = 'ChessComGames'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    url = Column(String(44), unique=True, index=True)
    pgn = Column(String)
    time_control = Column(String, index=True)
    end_time = Column(DateTime)
    rated = Column(Boolean)
    fen = Column(String)
    time_class = Column(String, index=True)
    rules = Column(String)
    white_rating = Column(Integer)
    white_result = Column(String, index=True)
    white_id = Column(String)
    white_username = Column(String, index=True)
    black_rating = Column(Integer)
    black_result = Column(String, index=True)
    black_id = Column(String)
    black_username = Column(String, index=True)

    def __init__(self,
                 url, pgn, time_control, end_time, rated, fen, time_class, rules,
                 white_rating, white_result, white_id, white_username,
                 black_rating, black_result, black_id, black_username):
        self.id = url.split('/')[-1]
        self.url = url
        self.pgn = pgn
        self.time_control = time_control
        self.end_time = datetime.datetime.fromtimestamp(end_time)
        self.rated = rated
        self.fen = fen
        self.time_class = time_class
        self.rules = rules
        self.white_rating = white_rating
        self.white_result = white_result
        self.white_id = white_id
        self.white_username = white_username
        self.black_rating = black_rating
        self.black_result = black_result
        self.black_id = black_id
        self.black_username = black_username


def main():
    return


if __name__ == '__main__':
    main()
