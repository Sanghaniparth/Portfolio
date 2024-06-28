from django.shortcuts import render,redirect
from pymongo.server_api import ServerApi
# import pandas as pd
import pymongo
from .models import Contact

uri = "mongodb+srv://parthsanghani01:P%40rth1234@portfolio.m8hgkyf.mongodb.net/"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
mydb = client['Portfolio']
mycol = mydb['Contact']

def index(request):
    if request.method=="POST":
        x={}
        uname=request.POST['name']
        uemail=request.POST['email']
        unumber=request.POST['number']
        umessgae=request.POST['message']
        x = {
            "Name":uname,
            "Email":uemail,
            "Number":unumber,
            "Message":umessgae
        }
        insert = mycol.insert_one(x)
        sql=Contact(name=uname,email=uemail,number=unumber,message=umessgae)
        sql.save()
        return render(request,"index.html")
       
    return render(request,"index.html")


