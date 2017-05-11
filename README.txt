

Udacity Fullstack Nanodegree
Project 3: Item Catalog
by Perry Kong..
apk29@hotmail.com
2017, May 10
Version 1

This is an application that implements a web app that provides a list of items within various categories. It incorporates the concepts 
CRUD (Create, Read, Update, & Delete) operations, registration and authentication through Google & Facebook.

To use this program you must have the follwoing programs installed:
1. Python 2.7
2. Virtual Box
3. Vagrant


Follow the following direction:

1. Clone or download this project from the following location:
   https://github.com/apk29/item_catalog_project
2. Located the project into your desired location in your working drive.
3. In terminal (MAC) or CMD (PC), be in the drive you just put the downloaded file.
4. Issue the following command to get into the virtual machine (VM)
	vagrant up
	vagrant ssh
	cd /vagrant
	python database_setup.py
	python model_catalog.py (database information)
	python main.py
	
5. Open your favorite web browser and enter the following address:
	http://localhost:5000/