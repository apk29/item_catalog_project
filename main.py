from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
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
APPLICATION_NAME = "Restaurant Menu Application"


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# @app.route('/')
# @app.route('/restaurant/JSON')
# def restaurantsJSON():
# 	restaurants = session.query(Restaurant).all()
# 	return jsonify(restaurants= [r.serialize for r in restaurants])
		
# #New Restaurant, JSON    
# @app.route('/restaurants/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
# 	restaurant = session.query(Restaurant).filter_by(
# 		id=restaurant_id).one()
# 	items = session.query(MenuItem).filter_by(
# 		restaurant_id=restaurant_id).all()
# 	return jsonify(MenuItems=[i.serialize for i in items])

# #Edit Restaurant, JSON
# @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
# def menuItemJSON(restaurant_id, menu_id):
# 	menuItem = session.query(MenuItem).filter_by(id=restaurant_id).one()
# 	return jsonify(MenuItems=menuItem.serialize)

@app.route('/')
@app.route('/category/')
def showCategory():
	categories = session.query(Category).all()
	items = session.query(Item).filter_by(category_id=category.id)
	output = ''
	for i in items:
		output += i.name
		output += '</br>'
	return output
	#This page will show all my restaurants"
	# return render_template('category.html', categories=categories)
	
# @app.route('/restaurant/new/', methods=['GET', 'POST'])
# def newCategory():
# # 	if request.method == 'POST':
# # 		newRestaurant = Restaurant(name=request.form['name'])
# # 		session.add(newRestaurant)
# # 		session.commit()
# # 		flash("New Restaurant Added!")
# # 		return redirect(url_for('showRestaurants'))
# # 	else:
# # 		return render_template('newRestaurant.html')
# # 	 # return "This page will be for making a NEW restaurant"
# # 	# return render_template('newrestaurant.html', restaurants=restaurants) Old render_template
# 	return "Hello, World2"
# @app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
# def editRestaurant(restaurant_id):
# 	editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	if request.method == 'POST':
# 		if request.form['name']:
# 			editedRestaurant.name = request.form['name']
# 		# session.add(editRestaurant)
# 		# session.commit()
# 		# flash("A Restaurant Name has been edited!")
# 		return redirect(url_for('showRestaurants'))
# 	else:
# 		return render_template('editRestaurant.html', restaurant=editedRestaurant)
# 	# restaurant_id = 1
# 	# return "This page will be for editing restaurant %s" % restaurant_id
# 	# return render_template('editRestaurant.html', restaurants=restaurants)

# @app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
# def deleteRestaurant(restaurant_id):
# 	RestaurantDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	if request.method == 'POST':
# 		session.delete(RestaurantDelete)
# 		session.commit()
# 		return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
# 	else:
# 		return render_template('deleterestaurant.html', restaurant=RestaurantDelete)
# 	# restaurant_id = 2
# 	# return "This page will be for deleting restaurant %s" % restaurant_id
# 	# return render_template('deleteRestaurant.html', restaurants=restaurants)

# @app.route('/restaurant/<int:restaurant_id>/')
# @app.route('/restaurant/<int:restaurant_id>/menu/')
# def showMenu(restaurant_id):
# 	restaurant=session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	items=session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
# 		# restaurant_id = 3
# 	# return "This page is the menu for restaurant %s" % restaurant_id
# 	return render_template('menus.html', items=items, restaurant=restaurant)

# @app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
# def newMenuItem(restaurant_id):
# 	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	if request.method == 'POST':
# 		newItem = MenuItem(name=request.form['name'], 
# 							description=request.form['description'],
# 							price=request.form['price'], 
# 							course=request.form['course'], 
# 							restaurant_id=restaurant.id)
# 		session.add(newItem)
# 		session.commit()
# 		flash('New Menu %s Item Created' % (newItem.name))
# 		return redirect(url_for('showMenu', restaurant_id=restaurant.id))
# 	else:
# 		return render_template('newMenuItem2.html', restaurant=restaurant)
# #   # restaurant_id = 4
# #   # return "This page is for making new menu item for retaurant %s" % restaurant_id
# 	# return render_template('newMenuItem2.html', items=items, restaurant=restaurant)

# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):
# 	editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
# 	# restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	if request.method == 'POST':
# 		if request.form.get('name'):
# 			editedItem.name = request.form['name']
# 		if request.form.get('description'):
# 			editedItem.description = request.form['description']
			
# 		if request.form.get('price'):
# 			editedItem.price = request.form['price']
# 		if request.form.get('course'):
# 			editedItem.course = request.form['course']
		
# 		session.add(editedItem)
# 		session.commit()
# 		flash("Menu Item Edited")
# 		return redirect(url_for('showMenu', restaurant_id=restaurant_id))
# 	else:
# 		return render_template('editMenuItem2.html',  
# 								restaurant_id=restaurant_id, menu_id=menu_id,
# 								item = editedItem)
# #   # restaurant_id = 4
# #   # menu_id= 5
# #   # return "This page is for is for editing menu item %s" % menu_id   
# 	# return render_template('editMenuItem2.html', restaurant=restaurant, item=item)

# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
# def deleteMenuItem(restaurant_id, menu_id):
# 	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
# 	deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
# 	if request.method == 'POST':
# 		session.delete(deleteItem)
# 		session.commit()
# 		flash("menu Item Deleted")
# 		return redirect(url_for('showMenu', restaurant_id=restaurant_id, item=deleteItem ))
# 	else:
# 		return render_template('deleteMenuItem2.html', restaurant=restaurant, item = deleteItem)


if __name__ == '__main__':
    
    app.debug = True
    app.run(host='0.0.0.0', port=5000)