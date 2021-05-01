import sqlalchemy as sa
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

from . import schemas

# ^^ declarative_base also available from sqlalchemy.orm if you have 1.4+

Base = declarative_base()


class Zoo(Base):
    __tablename__ = "zoos"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String)
    animals = sa.orm.relationship("Animal", back_populates="zoo", order_by="desc(Animal.weight)")

    def __repr__(self):
        return repr(schemas.Zoo.from_orm(self))


class Animal(Base):
    __tablename__ = "animals"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    weight = sa.Column(sa.Integer)
    zoo_id = sa.Column(sa.Integer, sa.ForeignKey("zoos.id"))
    zoo = sa.orm.relationship("Zoo", back_populates="animals")

    def __repr__(self):
        return repr(schemas.Animal.from_orm(self))
