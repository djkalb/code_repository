
from ast import Str
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, Boolean, ForeignKey, insert, select, func
from sqlalchemy.orm import Session, sessionmaker, registry, declarative_base, relationship
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Session = sessionmaker(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email_address= Column(String(80), unique=True)
    passkey = Column(String(30))
    trusted = Column(Boolean)
    algorithms = relationship("Algorithm", back_populates="user")
    def __repr__(self):
        return f"User(id={self.id!r}, email_address={self.email_address!r}, username={self.username!r})"

class Algorithm(Base):
    __tablename__ = "algorithms"
    id = Column(Integer, primary_key=True)
    description = Column(String(210), nullable=False)
    clean_description = Column(String)
    language = Column(String(30), nullable=False)
    code_body = Column(String(3000), nullable=False)
    useful = Column(Integer)
    privacy = Column(String(25), default="public")
    user_id = Column(ForeignKey('users.id'))

    user = relationship("User", back_populates="algorithms")
    def __repr__(self):
        return f"Algorithm(id={self.id!r}, description={self.description!r}, language={self.language}, code_body={self.code_body})"

Base.metadata.create_all(engine)
# def add_instance(obj):
#     Session.add(obj)
alg = Algorithm()
alg.id = 3
alg.description = "this is my description"
alg.language = "python"
alg.code_body = """repos is a console app designed to add and search code algorithms and other helpful tools.
            accepted arguments are add, search, config, view, and -h for help which can be called for each method individually. 
            call repos search <search>, <language> etc. can only call one function at a time
"""
with Session.begin() as sesh:
    sesh.add(alg)
    sesh.commit()
