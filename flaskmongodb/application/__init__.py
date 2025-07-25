from flask import Flask
from flask_pymongo import PyMongo
app=Flask(__name__)

app.config["SECRET_KEY"]='9aaeb5f6c2671ea9c3b0c22c6ac037ad46404f16'
app.config["MONGO_URI"]='mongodb+srv://vancyferns20:k4vHWwPyqy8qYMgm@cluster0.uxp4rpj.mongodb.net/myFirstDatabase'

#setup mongodb
mongodb_client=PyMongo(app)
db=mongodb_client.db
from application import routes