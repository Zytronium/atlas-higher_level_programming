#!/usr/bin/python3
"""
module for task 13
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    usrnm = argv[1]  # username
    pswrd = argv[2]  # password
    db_nm = argv[3]  # database name
    host = "localhost"  # host name; needed to shorten line 17 to <= 80 chars

    engine = create_engine(f'mysql+mysqldb://{usrnm}:{pswrd}@{host}/{db_nm}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    states = Session().query(State).filter(State.name.like('%a%')).all()

    for state in states:
        Session().delete(state)

    Session().commit()
    Session().close()
