#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
(case-insensitive) from the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, db_name):
    """
    Connects to the MySQL database and prints all
    State objects that contain the letter 'a',
    ordered by id in ascending order.
    """
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 9-model_state_filter_a.py <username> <password> <database>")
        sys.exit(1)
    list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
