from flask import Flask, render_template, jsonify, redirect
from pymongo import MongoClient
import scrape_mars

app = Flask(__name__)

# Use pymongo to set up mongo connection
mongo_url = "mongodb://localhost:27017"
client = MongoClient(mongo_url)
db = Web_Scraping_HW


@app.route("/scrape")
def scrape():
    mars = db.Web_Scraping_HW
    mars_data = Web_Scraping_HW.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code = "302")

@app.route("/")
def index():
    mars = db.Web_Scraping_HW.find_one()
    return render_template("index.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)