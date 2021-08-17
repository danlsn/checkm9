from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, ForeignKey
from base import Session, Base, engine


class ChessComOpening(Base):
    __tablename__ = 'ChessComOpenings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    eco_code = Column(String(4))
    eco_name = Column(String)
    eco_url = Column(String)


def main():
    return


if __name__ == '__main__':
    main()
