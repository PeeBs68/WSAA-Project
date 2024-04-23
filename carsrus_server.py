from flask import Flask, url_for, request, redirect, abort

# Import dao here

app = Flask(__name__, static_url_path='', static_folder='staticpages')


# Do stuff here

if __name__ == "__main__":
    app.run(debug=True)

