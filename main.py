import requests
import requests_cache
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from base import Base, engine, Session
from chessdotcom import *
import logging

# Load Environment Variables
from models.chess_com_game import ChessComGame

load_dotenv()

logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.DEBUG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


requests_cache.install_cache(cache_name='cache', backend='sqlite', expire_after=600)


def flatten(t):
    return [item for sublist in t for item in sublist]


def insert_archive_urls(username: str):
    from models.chess_com_game_archive import ChessComGameArchive
    Base.metadata.create_all(engine)
    s = Session()
    archive_urls = get_player_game_archives(username).archives
    print(f'''Archive URLs: {archive_urls}''')
    archives = [ChessComGameArchive(archive_url) for archive_url in archive_urls]
    s.begin()
    for archive in archives:
        try:
            print(f'''Current Archive: {archive.url}''')
            s.merge(archive)
            # s.commit()
        except SQLAlchemyError as err:
            logging.warning("SQLAlchemyError: {}".format(err.orig.pgerror))
            s.rollback()
            pass
        s.commit()
    return


def get_game_archive_urls(username: str):
    from models.chess_com_game_archive import ChessComGameArchive
    s = Session()
    q = s.query(ChessComGameArchive.games).filter(ChessComGameArchive.username.like(username)).all()
    game_arrays = flatten(q)
    url_list = flatten(game_arrays)
    return url_list


def insert_player_profile(username: str):
    from models.chess_com_player_profile import ChessComPlayerProfile
    Base.metadata.create_all(engine)
    s = Session()
    profile = ChessComPlayerProfile(username)
    s.merge(profile)
    s.commit()


def insert_single_game(game: dict):
    from models.chess_com_game import ChessComGame
    Base.metadata.create_all(engine)
    g = game
    s = Session()
    game_object = ChessComGame(g.get('url'), g.get('pgn'), g.get('time_control'), g.get('end_time'),
                               g.get('rated'), g.get('fen'), g.get('time_class'), g.get('rules'),
                               g.get('white').get('rating'), g.get('white').get('result'),
                               g.get('white').get('@id'), g.get('white').get('username'),
                               g.get('black').get('rating'), g.get('black').get('result'),
                               g.get('black').get('@id'), g.get('black').get('username'), )
    s.merge(game_object)
    return game_object


def insert_many_games(games: list):
    from models.chess_com_game import ChessComGame
    Base.metadata.create_all(engine)
    s = Session()
    game_ids = [g.get('url').split('/')[-1] for g in games]
    game_objects = [ChessComGame(g.get('url'), g.get('pgn'), g.get('time_control'), g.get('end_time'),
                                 g.get('rated'), g.get('fen'), g.get('time_class'), g.get('rules'),
                                 g.get('white').get('rating'), g.get('white').get('result'),
                                 g.get('white').get('@id'), g.get('white').get('username'),
                                 g.get('black').get('rating'), g.get('black').get('result'),
                                 g.get('black').get('@id'), g.get('black').get('username'), ) for g in games]
    for game in game_objects:
        s.merge(game)
    s.commit()
    return game_objects


def insert_player_games(username: str):
    from models.chess_com_game import ChessComGame
    Base.metadata.create_all(engine)
    s = Session()
    archive_urls = get_player_game_archives(username).archives
    for archive_url in archive_urls:
        urls_expire_after = {
            f'''https://api.chess.com/pub/player/*/games/{datetime.now().strftime('%Y/%m/')}''': 0
        }
        req = requests_cache.CachedSession('cache/archive_url_cache',
                                           backend='filesystem',
                                           urls_expire_after=urls_expire_after)
        r = req.get(archive_url).json()
        games = [archive for archive in r.get('games')]
        insert_many_games(games)
    return


def get_unique_players():
    s = Session()
    q_white = select([ChessComGame.white_username])
    q_black = select([ChessComGame.black_username])
    q = q_white.union(q_black).alias('username')
    unique_players = s.query(q).all()
    return unique_players


if __name__ == '__main__':
    # insert_archive_urls('danlsn')
    # list = get_game_archive_urls('danlsn')
    # for user in ['gothamchess', 'hikaru', 'danlsn']:
    #     insert_player_profile(user)
    # pass
    insert_player_games('QTCinderella')
    # ['danielnaroditsky', 'ohmylands', 'chuckmoulton', 'danlsn', 'malikidesc', 'gothamchess', 'hikaru', 'ChessBrah',
    # 'KVNB', 'annacramling', 'ludwig'] ['venancioortega', 'agadmator', 'penguingm1', 'danielnaroditsky',
    # 'ohmylands', 'chuckmoulton', 'danlsn', 'malikidesc', 'gothamchess', 'hikaru', 'ChessBrah', 'KVNB',
    # 'annacramling', 'ludwig','GMCanty', 'GMHess', 'Anna_Chess', 'SamCopeland', 'AlexandraBotez',
    # 'GMBenjaminFinegold', 'QTCinderella', 'MichelleKhare', 'DanielRensch', 'bobbybojanglles', 'viditchess',
    # 'GMHikaruOnTwitch','erichansen', 'anishgiri', 'samayraina', 'firouzja2003'] for player in ['Lud-Skywalker',
    # 'mrbeastreal', 'rubiuszx', 'mobamba604', 'moistCr1tikal', 'xQcow', 'RainnWilson', #
    # 'sardochesti', 'neeko', 'Benjyfishy1', 'codemikoattwitch', 'turbofisto', 'bobbyhall', 'dnegs', #
    # 'TheMyth', 'pokimane']: for player in ['gothamchess']: insert_player_profile(player) insert_archive_urls(
    # player) insert_player_games(player) unique_players = get_unique_players() for player in unique_players: print(
    # f'''Current Player: {player[0]}''') try: print(f'''Inserting {player[0]} Profile''') insert_player_profile(
    # player[0]) print(f'''Inserting {player[0]} Archive URLs''') insert_archive_urls(player[0]) print(f'''Inserting
    # {player[0]} Games''') insert_player_games(player[0]) except ChessDotComError: pass
