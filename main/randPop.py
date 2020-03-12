from main import db
from main.models import Item, Company
from random import randint
import random

itemNames = ['Ginger', 'Celery', 'Chicken', 'Pork', 'Soup', 'Tomato', 'Orange', 'Beef']
companyNames = ['Pepsi', 'Mars', 'Kellog']

def randPop():
    """
    randPop() makes some example Company and Item objects using randint and a random choice.
    
    The first loop creates all the companies.
    
    Within the second loop, each Item object is instantiated, and then added to the database.
    After the second  loop, all changes to the database are committed if possible. If changes aren't possible, the database performs a rollback to before the session.
    """
    db.drop_all()
    db.create_all()

    for x in range(len(companyNames)):
        newCompany = Company(companyName=companyNames[x], country='United States')
        db.session.add(newCompany)
    
    try:
        db.session.commit()
    except:
        db.session.rollback()

    for x in range(20):
        newItem = Item(upc=randint(1,5000), parentCompany=random.choice(companyNames), itemName=random.choice(itemNames), price=randint(10,20)+.99, weight=randint(1,20))
        print(newItem)
        db.session.add(newItem)

    try:
        db.session.commit()
    except:
        db.session.rollback()