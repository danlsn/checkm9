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

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey, TIMESTAMP, func
from chessdotcom import *
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
    last_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, username):
        player = get_player_profile(username).json['player']
        self.id = player['@id']
        self.url = player['url']
        self.username = player['username']
        self.player_id = player['player_id']
        self.title = player.get('title', None)
        self.status = player['status']
        self.name = player.get('name')
        self.avatar = player.get('avatar')
        self.location = player.get('location', None)
        self.country = player['country']
        self.joined = datetime.fromtimestamp(player['joined'])
        self.last_online = datetime.fromtimestamp(player['last_online'])
        self.followers = player['followers']
        self.is_streamer = player['is_streamer']
        self.twitch_url = player.get('twitch_url', None)
        self.fide = player.get('fide', None)




def main():
    player_profile = get_player_profile('gothamchess')
    player_profile2 = get_player_profile('danlsn')
    gothamchess = ChessComPlayerProfile('gothamchess')
    return


if __name__ == '__main__':
    main()
