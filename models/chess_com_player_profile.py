"""
{
  "@id": "URL", // the location of this profile (always self-referencing)
  "url": "URL", // the chess.com user's profile page (the username is displayed with the original letter case)
  "username": "string", // the username of this player
  "player_id": 41, // the non-changing Chess.com ID of this player
  "title": "string", // (optional) abbreviation of chess title, if any
  "status": "string", // account status: closed, closed:fair_play_violations, basic, premium, mod, staff
  "name": "string", // (optional) the personal first and last name
  "avatar": "URL", // (optional) URL of a 200x200 image
  "location": "string", // (optional) the city or location
  "country": "URL", // API location of this player's country's profile
  "joined": 1178556600, // timestamp of registration on Chess.com
  "last_online": 1500661803, // timestamp of the most recent login
  "followers": 17 // the number of players tracking this player's activity
  "is_streamer": "boolean", //if the member is a Chess.com streamer
  "twitch_url": "Twitch.tv URL",
  "fide": "integer" // FIDE rating
}
"""

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey
from base import Session, Base, engine


class ChessComPlayerProfile(Base):
    __tablename__ = 'ChessComPlayerProfiles'

    id = Column(String, primary_key=True)
    url = Column(String)
    username = Column(String)
    player_id = Column(Integer)
    title = Column(String)
    status = Column(String)
    name = Column(String)
    avatar = Column(String)
    location = Column(String)
    country = Column(String)
    joined = Column(DateTime)
    last_online = Column(DateTime)
    followers = Column(Integer)
    is_streamer = Column(Boolean)
    twitch_url = Column(String)
    fide = Column(Integer)
    pass


def main():
    return


if __name__ == '__main__':
    main()
