from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connect = 'mysql+pymysql://root:txjssk13@127.0.0.1:3306/test'
engine = create_engine(connect)


Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__= 'user_4'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


def run():
    info = session.query(User).filter(User.id < 5).all()
    if info:
        session.query(User).filter(User.id == 1).update({User.name: 'dsadada'})
        session.commit()
        print('查找到了')


if __name__ == '__main__':
    # User.metadata.create_all(engine)
    run()







