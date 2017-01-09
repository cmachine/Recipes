from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Recipe(Base):
  __tablename__ = 'recipe'
  id = Column(Integer, primary_key=True)
  name = Column(String)

engine = create_engine('sqlite:///recipies.db', echo=True)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_recipe = Recipe(name='Taco Salad')
session.add(new_recipe)
session.commit()
