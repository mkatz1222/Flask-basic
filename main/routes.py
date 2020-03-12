from flask import render_template
from main import app, db
from main.models import Item, Company
from random import randint
from main.randPop import randPop

@app.route("/")
@app.route("/index")
def index():
    """
    The index route is the homepage for the flask site. 
    Below, randPop() is called from another file. randPop() creates all the tables and fills them with some random items.
        - Within randPop(), the database deletes and then creates all tables everytime it is called. This isn't necessary.
        I only included them to show what the commands are.
        - Although, before any object can be added to the database all tables must be created like in line 16 of randPop.py
        
    There are two examples of querying the whole database below. Both queries perform the same function. 
    When you only want to query one class, it's simpler to use the first query.
    If any joins are being used, you'll need to work with the structure of the second example.
    """
    randPop()
    allItems = Item.query.all()
    #allItems = db.session.query(Item).all()
    return render_template('index.html', items=allItems)

@app.route("/joinExample")
def joinExample():
    """
    The joinExample route shows how to make a basic join query with a where clause.
    I think the SQL equivalent would be "SELECT * FROM Item,Company WHERE parentCompany = companyName"
    """
    itemJoinCompany = db.session.query(Item, Company).filter(Item.parentCompany == Company.companyName)
    return render_template('joinExample.html', itemJoinCompany=itemJoinCompany)