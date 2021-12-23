from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo 
import scrape_mars

app =  Flask(__name__)

# use flask pymongo to set up the connection to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    #access information from the database
    mars_data = mongo.db.marsData.find_one()
    print(mars_data)
    return "Flask data loaded"

@app.route("/scrape")
def scrape():
    # reference to a database collection
    marsTable = mongo.db.marsData

    # drop the table if it exist
    mongo.db.marsData.drop()

    # call scrape mars script
    mars_data = scrape_mars.scrape_all()
    
    # take the dictionary and load into mongoDB
    marsTable.insert_one(mars_data)

    # go to the index route
    return redirect("/")

if __name__ == "__main__":
    app.run()

