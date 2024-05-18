Repository Name: WSAA-Project
Author: Phelim Barry

This readme contains details of the WSAA-Project repository

Purpose:
    The purpose of this project is to build an application that provides an online user interface to perform CRUD operations on a database using a) a Flask server that provides a Restful API and b) a web page that allows the user to interact with that Restful API.

Running the application:
    There are two options to run the code and view the functionality. To run it locally, firstly start the flask server (python carsrus_server.py), ensure the appropriate database is online and available then use the following link to access the web page - http://127.0.0.1:5000/carsrus.html   
    Alternatively, the application is being hosted on pythonanywhere and can be accessed via this link - https://phelimbarry.pythonanywhere.com/carsrus.html

The following files are contained in this repository:
    carsrus_dao.py - manages all database connectivity and sql scripts.
    carsrus_server.py - flask server 
    carsrus.html - web page
    config.py (hidden from GitHub) - contains database connection details (username, password etc).
    carsrus_functions.js - single javascript file to store all functions used by the web page.
    carsrus_styles.css - describes how the web page should display different HTML elements.

Modules installed/imported:
    mysql.connector
    jsonify, abort, Flask, request (flask)



