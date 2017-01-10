from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Recipe(Base):
  __tablename__ = 'recipe'
  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True)

class Ingredient(Base):
  __tablename__ = 'ingredient'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  qty = Column(Float)
  unit = Column(String)
  recipe = Column(String, ForeignKey('recipe.name'))

engine = create_engine('sqlite:///recipies.db', echo=True)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
taco_salad = Recipe(name='Taco Salad')
lettuce = Ingredient(name='Lettuce', qty=1, unit='head', recipe='Taco Salad')
session.add(taco_salad)
session.add(lettuce)
session.commit()
