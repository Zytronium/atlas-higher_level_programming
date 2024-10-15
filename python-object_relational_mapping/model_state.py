#!/usr/bin/python3
"""
module for task 6
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    class representing a state, inheriting from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    # test_val = id
    # print(id)
    # print(name)
    # print(test_val)

if __name__ == '__main__':
    testState = State(name="Oklahoma")
    print(testState.id)
    print(testState.name)
    # print(testState.test_val)
