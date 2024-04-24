# Flask Server
# author: Phelim Barry

from flask import Flask, url_for, request, redirect, abort
from carsrus_dao import carsiteDAO

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def index():
    return("Hello there")

# Get all cars
@app.route('/carsrus', methods = ['GET'])
def getall():
    return("Get all")

# Get car by ID
@app.route('/carsrus/<int:id>', methods = ['GET'])
def findbyid(id):
    return(f"Find by ID {id}")

# Create a car
@app.route('/carsrus', methods = ['POST'])
def create():
    # read JSON...need to test this using POSTMAN so as to add the details in JSON format
    jsonstring = request.json

    return(f"Create {jsonstring}")

# Update a car
@app.route('/carsrus/<int:id>', methods = ['PUT'])
def update(id):
    # read JSON...need to test this using POSTMAN so as to add the details in JSON format
    jsonstring = request.json

    return(f"Update {id} {jsonstring}")

# Delete a car
@app.route('/carsrus/<int:id>', methods = ['DELETE'])
def delete(id):
    return(f"Delete by ID {id}")

if __name__ == "__main__":
    app.run(debug=True)

