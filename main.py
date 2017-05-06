from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, ItemInformation, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
# import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
	open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Category Application"


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON APIs to view Category Information
@app.route('/category/<int:category_id>/item/JSON')
def categoryItemJSON(category_id):
	return "Category JSON Info"


@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
	return "Category Category Item JSON"

@app.route('/category/JSON')
def categorysJSON():
	return "Category JSON"

# Show all category
@app.route('/')
@app.route('/category/')
def showCategories():
	categories = session.query(Category).order_by(asc(Category.name))
	if 'username' not in login_session:
		return render_template('publiccategories.html', categories=categories)
	else:
		return render_template('categories.html', categories=categories)

#Creat new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCatelgory():
	return "New Category"


#Edit Category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
	return "Edit Category"

#Delete Category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deletecategory(category_id):
	return "Delete Category"

#Show Items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/item/')
def showItem(category_id):
	category = session.query(Category).filter_by(id=category_id).one()
	creator = getUserInfo(category.user_id)
	items = session.query(ItemInformation).filter_by(
		category_id=category_id).all()
	if 'username' not in login_session or creator.id != login_session['user_id']:
		return render_template('publiciteminformation.html', items=items, category=category)
	else:
		return render_template('iteminformation.html', items=items, category=category, creator=creator)


#Create New Items
@app.route('/category/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItemIformation(category_id):
	return "Create New Items"

# Edit a item item
@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editItemInformation(category_id, item_id):
	return "Edit item"

# Delete item
@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItemInformation(category_id, item_id):
	return "Delete item"


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)