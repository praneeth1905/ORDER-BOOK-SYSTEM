import email
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app=Flask(__name__)
app.config['SECRET_KEY']="random"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.sqlite3'

db=SQLAlchemy(app)

class orders(db.Model):
    id=db.Column('user_id', db.Integer, primary_key=True)
    executedqty=db.Column(db.Integer)
    name=db.Column(db.String(20))
    book=db.Column(db.String(20))
    type=db.Column(db.String(20))
    cost=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    status=db.Column(db.String(20))
    orderdate=db.Column(db.String(10))

def __init__(self,name,book,type,cost,quantity):
    self.name=name
    self.book=book
    self.type=type
    self.cost=cost
    self.quantity=quantity
    self.executedqty=0
    self.status='PLACED'
    self.orderdate='29-01-2022'

@app.route('/',methods=['POST','GET'])
@app.route('/customer',methods=['POST','GET'])
def customer():
    if request.method=='POST':
        order=orders(name=request.form.get('name'),book =  request.form.get('book-names'), type=request.form.get('type'), cost =request.form.get('cost'),quantity= request.form.get('quantity'),executedqty=0,status='PLACED',orderdate='29-01-2022')
        db.session.add(order)
        db.session.commit()
        flash('books added','success')
    return render_template('customer.html')

@app.route('/admin',methods=['POST','GET'])
def admin():
    
    return render_template("admin.html",orders=orders.query.all())

@app.route('')


if __name__== '__main__':
    db.create_all()
    app.run(debug=True)
    