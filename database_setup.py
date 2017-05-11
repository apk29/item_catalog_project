import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250))
    picture = Column(String(250))

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    item = relationship('ItemInformation', cascade='all, delete-orphan', passive_deletes=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

class ItemInformation(Base):
    __tablename__ = "item_information"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000))
    image = Column(String(250))
    price = Column(String(8))
    make = Column(String(250))
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id',
                         ondelete='CASCADE'), nullable=False)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price
        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)