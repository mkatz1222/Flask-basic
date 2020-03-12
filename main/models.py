from main import db

"""
The classes below describe tables within the sqlite database.

Each column in the table is represented as a field within the class.

The __repr__ functions are for printing/debugging purposes. When you print or display an object, the __repr__
function will display the object in an easily readable format. 
"""

class Item(db.Model):
    __tablename__ = 'Item'
    upc = db.Column(db.Integer, primary_key=True)
    parentCompany = db.Column(db.String, db.ForeignKey('company.companyName'))
    itemName = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float(), nullable=True)
    weight = db.Column(db.Integer)

    def __repr__(self):
        return f'Item(upc:{self.upc}, company:{self.parentCompany}, name: {self.itemName}, price: {self.price}, weight: {self.weight})'

class Company(db.Model):
    companyName = db.Column(db.String, primary_key=True)
    country = db.Column(db.String)
    companyItem = db.relationship('Item', cascade='all,delete', backref='company')

    def __repr__(self):
        return 'Company(companyName:' + self.companyName + ', country:' + self.country + ')'
