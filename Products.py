from werkzeug.wrappers import Request, Response
from flask import Flask, jsonify,request
from pymongo import MongoClient
from bson.json_util import dumps

name = str

def Products(name):
    client=MongoClient('localhost', 27017)
    db = client["Products"]
    
    #creating collections and inserting values into it
    Product = db["Products"]
    #record=[{"proname": "oil", "probrand": "gemini", "proprice": 120, "proexp_date": "25-12-21"},{"proname": "toothpaste", "probrand": "closeup", "proprice": 50, "proexp_date": "12-08-21"},{"proname": "soap", "probrand": "dove", "proprice": 65, "proexp_date": "24-09-21"},{"proname": "shampoo", "probrand": "sunsilk", "proprice": 80, "proexp_date": "11-10-21"},{"proname": "rice", "probrand": "indiagate", "proprice": 150, "proexp_date": "03-09-21"}]#
    
    soap = db["soap"]
    #record=[{"proname": "soap", "probrand": "lux", "proprice": 35, "proexp_date": "25-12-21"},{"proname": "soap", "probrand": "pears", "proprice": 40, "proexp_date": "24-10-21"},{"proname": "soap", "probrand": "vim", "proprice": 15, "proexp_date": "18-04-21"},{"proname": "soap", "probrand": "surfexcel", "proprice": 20, "proexp_date": "09-10-21"},{"proname": "soap", "probrand": "santoor", "proprice": 25, "proexp_date": "15-07-21"}]#
    
    #updating shampoo by 10rs
    shampoo = db["shampoo"]
    #record=[{"proname": "shampoo", "probrand": "sunsilk", "proprice": 90, "proexp_date": "07-11-21"},{"proname": "shampoo", "probrand": "loreal", "proprice": 120, "proexp_date": "13-12-21"}]#
    
def getAllProducts():
    client=MongoClient('localhost', 27017)
    db = client["Products"]
    collection = db["collection"]
    products = collection.find()
    return dumps(Products)

def AddProduct(name,price,exp_date):
    client = MongoClient('localhost', 27017)
    db = client["Productdb"]
    collection = db["collection"]
    record= {"proName": name, "probrand": "brand", "proPrice": price, "proExp_date": "exp_date"}
    collection.insert_one(record)
    return jsonify({'inserted': true})
                
