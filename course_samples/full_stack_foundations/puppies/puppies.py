from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Let SqlAlchemy knows our DB Classes are Special DB classes
Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    zipCode = Column(String(5), nullable=False)
    website = Column(String(250))


class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(Boolean)
    weight = Column(Integer)
    picture = Column(String(250))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


# Instance to Database we are using
engine = create_engine('sqlite:///puppyshelter.db')
# Go into de DB and add the new classes added as new tables
Base.metadata.create_all(engine)
