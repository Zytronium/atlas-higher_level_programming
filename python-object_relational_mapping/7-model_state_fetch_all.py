#!/usr/bin/python3
"""
module for task 7
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    usrnm = argv[1]  # username
    pswrd = argv[2]  # password
    db_nm = argv[3]  # database name
    host = "localhost"  # host name; needed to shorten line 18 to <= 80 chars
    # yes, this variable only saves 2 chars on line 18

    engine = create_engine(f'mysql+mysqldb://{usrnm}:{pswrd}@{host}/{db_nm}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    states = Session().query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    Session().close()
