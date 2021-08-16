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

from base import Session, Base, engine


class ChessComGame(Base):
    pass


def main():
    return


if __name__ == '__main__':
    main()
