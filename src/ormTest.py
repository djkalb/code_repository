
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, func
from sqlalchemy.orm import Session, sessionmaker, registry, declarative_base, relationship
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
register = registry()
Session = sessionmaker(engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)
sandy = User(name="sandy", fullname="Sandy Cheeks")
squidward = User(name="squidward", fullname ="Squidward Tentacles")
krabs = User(name= "Crusty", fullname="Crusty Crabs")
session = Session()
session.add(squidward)
session.add(krabs)
session.flush()
print(squidward.id)
squids = session.get(User, 1)
print(squids)
session.commit()
session.close()

with Session() as sesh:
    user = session.scalars(select(User)).first()
    stmt = select(User)
    result = sesh.execute(stmt)
    print(user)
    count = func.count(User.id)
    print(count)