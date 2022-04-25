from contextlib import nullcontext
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, registry

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
# metadata_obj = MetaData()
register = registry()
# with engine.connect() as conn:
#     result = conn.execute(text("select 'Hello World'"))
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x":2, "y":4}]
#     )
#     conn.commit()
    
# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
#     )
    
# with engine.begin() as conn:
#     result = conn.execute(text("select x, y from some_table"))
#     new_result = conn.execute(text("select x, y from some_table where y > :y"), {"y": 2})
# with engine.begin() as conn:
#     conn.execute(
#          text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#          [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
#      )
#     conn.commit()
# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y = 6)
# with engine.begin() as conn:
    
#     result = conn.execute(stmt)
# # Session is the ORM version of Connection -- engine is either passed in or Session can be an instance created using sessionmaker
# # which gets the engine passed in to it  
# with Session(engine) as session:
#     result = session.execute(stmt)
#     for row in result:
#         print(f"x = {row.x} and y = {row.y}")

# with Session(engine) as session:
#     result = session.execute(
#         text("UPDATE some_table SET y=:y WHERE x=:x"),
#         [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
#     )
#     session.commit()
# Session = sessionmaker(engine)
# user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column('id', Integer, primary_key = True),
#     Column('name', String(30)),
#     Column('fullname', String)
# )
# address_table = Table(
#     "address",
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('user_id', ForeignKey('user_account.id'), nullable=False),
#     Column('email_address', String, nullable=False)
# )
# metadata_obj.create_all(engine)
# print(user_table.c.keys())