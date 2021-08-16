"""
{
  "chess_daily": {
    /* stats object for games of rules "chess" and "daily" time-class */
  },
  "chess960_daily": {
    /* stats object for games of rules "chess960" and "daily" time-class */
  },
  "chess_blitz": {
    /* stats object for games of rules "chess" and "blitz" time-class */
  },
  "tactics": {
      "highest": {
          "rating": "integer",
          "date": "timestamp"
      },
      "lowest": {
          "rating": "integer",
          "date": "timestamp"
      }
  },
  "lessons":{
      "highest": {
          "rating": "integer",
          "date": "timestamp"
      },
      "lowest": {
          "rating": "integer",
          "date": "timestamp"
      }
  },
  "puzzle_rush": {
      "daily":{
          "total_attempts": "integer",
          "score": "integer"
       },
      "best": {
          "total_attempts": "integer",
          "score": "integer"
       }
   }
}

{
  "last": { // the current stats
    "date": 1509709165, // timestamp of the last rated game finished
    "rating": 1642, // most-recent rating
    "rd": 58 // the Glicko "RD" value used to calculate ratings changes
  },
  "best": { // the best rating achieved by a win
    "date": 1256228875, // timestamp of the best-win game
    "rating": 2065, // highest rating achieved
    "game": "URL" // URL of the best-win game
  },
  "record": { // summary of all games played
    "win": 177,  // number of games won
    "loss": 124, // number of games lost
    "draw": 21,  // number of games drawn
    "time_per_move": 18799, // integer number of seconds per average move
    "timeout_percent": 9.99 // timeout percentage in the last 90 days
  },
  "tournament": { // summary of tournaments participated in
    "count": 20,   // number of tournaments joined
    "withdraw": 1, // number of tournaments withdrawn from
    "points": 39,  // total number of points earned in tournaments
    "highest_finish": 1 // best tournament place
  }
}

{
  "chess_daily": {
    "last": {
      "rating": 1051,
      "date": 1626392242,
      "rd": 103
    },
    "best": {
      "rating": 1168,
      "date": 1624276445,
      "game": "https://www.chess.com/game/daily/341130047"
    },
    "record": {
      "win": 17,
      "loss": 4,
      "draw": 0,
      "time_per_move": 5234,
      "timeout_percent": 0
    }
  },
  "chess_rapid": {
    "last": {
      "rating": 966,
      "date": 1628318069,
      "rd": 57
    },
    "best": {
      "rating": 966,
      "date": 1628318069,
      "game": "https://www.chess.com/game/live/22056552777"
    },
    "record": {
      "win": 151,
      "loss": 112,
      "draw": 11
    }
  },
  "chess_bullet": {
    "last": {
      "rating": 778,
      "date": 1628832754,
      "rd": 47
    },
    "best": {
      "rating": 887,
      "date": 1624032059,
      "game": "https://www.chess.com/game/live/6412964266"
    },
    "record": {
      "win": 292,
      "loss": 280,
      "draw": 6
    }
  },
  "chess_blitz": {
    "last": {
      "rating": 938,
      "date": 1628845340,
      "rd": 34
    },
    "best": {
      "rating": 1012,
      "date": 1628082406,
      "game": "https://www.chess.com/game/live/12022452001"
    },
    "record": {
      "win": 484,
      "loss": 452,
      "draw": 41
    }
  },
  "fide": 0,
  "tactics": {
    "highest": {
      "rating": 1554,
      "date": 1625052773
    },
    "lowest": {
      "rating": 370,
      "date": 1608884088
    }
  },
  "lessons": {},
  "puzzle_rush": {
    "best": {
      "total_attempts": 25,
      "score": 22
    }
  }
}

"""

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Session, Base, engine


class ChessComPlayerStats(Base):
    __tablename__ = 'ChessComPlayerStats'

    id = Column(Integer, primary_key=True)
    dateTime = Column(DateTime)
    dailyLastRating = Column(Integer)
    dailyLastDate = Column(DateTime)
    dailyLastRd = Column(Integer)
    dailyBestRating = Column(Integer)
    dailyBestDate = Column(DateTime)
    dailyBestGame = Column(String)
    dailyRecordWin = Column(Integer)
    dailyRecordLoss = Column(Integer)
    dailyRecordDraw = Column(Integer)

    rapidLastRating = Column(Integer)
    rapidLastDate = Column(DateTime)
    rapidLastRd = Column(Integer)
    rapidBestRating = Column(Integer)
    rapidBestDate = Column(DateTime)
    rapidBestGame = Column(String)
    rapidRecordWin = Column(Integer)
    rapidRecordLoss = Column(Integer)
    rapidRecordDraw = Column(Integer)

    blitzLastRating = Column(Integer)
    blitzLastDate = Column(DateTime)
    blitzLastRd = Column(Integer)
    blitzBestRating = Column(Integer)
    blitzBestDate = Column(DateTime)
    blitzBestGame = Column(String)
    blitzRecordWin = Column(Integer)
    blitzRecordLoss = Column(Integer)
    blitzRecordDraw = Column(Integer)

    bulletLastRating = Column(Integer)
    bulletLastDate = Column(DateTime)
    bulletLastRd = Column(Integer)
    bulletBestRating = Column(Integer)
    bulletBestDate = Column(DateTime)
    bulletBestGame = Column(String)
    bulletRecordWin = Column(Integer)
    bulletRecordLoss = Column(Integer)
    bulletRecordDraw = Column(Integer)

    fide = Column(Boolean)

    tacticsHighestRating = Column(Integer)
    tacticsHighestDate = Column(DateTime)
    tacticsLowestRating = Column(Integer)
    tacticsLowestDate = Column(DateTime)
    puzzleRushBestTotalAttempts = Column(Integer)
    puzzleRushBestScore = Column(Integer)

    def __init__(self):
        pass


def main():
    s = Session()

    return


if __name__ == '__main__':
    main()
