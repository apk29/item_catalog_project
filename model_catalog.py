from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import *
from database_setup import User, Category, ItemInformation
from sqlalchemy.orm import sessionmaker
from database_setup import Base

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

session = DBSession()
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

# Create a session and connect to database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="George t Monkey", email="theMoney@madeupmonkey.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# Items for Watch
category1 = Category(user_id=1, name="Watches")

session.add(category1)
session.commit()

item2 = ItemInformation(user_id=1, name="Casio", description="chronograph",
                     price="$29.99", make="Japanese", category=category1)

session.add(item2)
session.commit()

item3 = ItemInformation(user_id=1, name="Timex", description="Expedition Rugged",
                     price="$39.99",  make="US", category=category1)

session.add(item3)
session.commit()

item4 = ItemInformation(user_id=1, name="Gear3", description="Android",
                     price="$239.99", make="Japanese", category=category1)

session.add(item4)
session.commit()

item5 = ItemInformation(user_id=1, name="Apple Watch", description="Apple OS",
                     price="$239.99", make="US", category=category1)

session.add(item5)
session.commit()

#Items for bikes

category2 = Category(user_id=1, name="Bicycles")
session.add(item2)
session.commit()

item1 = ItemInformation(user_id=1, name="Liv Lust Advanced 1", description="Moutain",
                     price="$577.99", make="US", category=category2)

session.add(item1)
session.commit()

item2 = ItemInformation(user_id=1, name="Corima", description="Road",
                     price="$5277.99", make="US", category=category2)

session.add(item2)
session.commit()

item3 = ItemInformation(user_id=1, name="Cannondale Quick 3", description="Hyrbrid",
                     price="$5277.99", make="UK", category=category2)

session.add(item3)
session.commit()

item4 = ItemInformation(user_id=1, name="Brennabor ", description="Standard",
                     price="$5277.99", make="Germany", category=category2)

session.add(item4)
session.commit()

item5 = ItemInformation(user_id=1, name="Brodie Bicycles ", description="Motorized",
                     price="$5277.99", make="US", category=category2)

session.add(item5)
session.commit()

# Items for Cars
category3 = Category(user_id=1, name="Cars")

session.add(category1)
session.commit()

item2 = ItemInformation(user_id=1, name="Corolla", description="Passenger Car",
                     price="$18000.00", make="Japanese", category=category3)

session.add(item2)
session.commit()

item3 = ItemInformation(user_id=1, name="Tacoma", description="Medium Truck",
                     price="$30000.00",  make="Japanese", category=category3)

session.add(item3)
session.commit()

item4 = ItemInformation(user_id=1, name="F-150", description="Full Sized Truck",
                     price="$23999.99", make="US", category=category3)

session.add(item4)
session.commit()

item5 = ItemInformation(user_id=1, name="FRS", description="Sports Car",
                     price="$24999.99", make="Japanese", category=category3)

session.add(item5)
session.commit()


session.add(item5)
session.commit()
print "added items!"