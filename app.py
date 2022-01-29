import email
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']="random"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.sqlite3'

db=SQLAlchemy(app)
open=True
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

def _init_(self,name,book,type,cost,quantity):
    self.name=name
    self.book=book
    self.type=type
    self.cost=cost
    self.quantity=quantity
    self.executedqty=0
    self.status='PLACED'
    self.orderdate='29-01-2022'

@app.route('/',methods=['POST','GET'])
def home():
        return render_template('index.html')

@app.route('/adm',methods=['POST','GET'])
def admlog():
        return render_template('adm-log.html')

@app.route('/cust',methods=['POST','GET'])
def custLog():
        return render_template('cust-log.html')

@app.route('/open',methods=['POST','GET'])
def opend():
    session['open']='1' 
    return redirect(url_for('customer'))

@app.route('/close',methods=['POST','GET'])
def close():
    session['open']='0'  
    return redirect(url_for('customer'))


@app.route('/customer',methods=['POST','GET'])
def customer():
    if request.method=='POST':        
            order=orders(name=request.form.get('name'),book =  request.form.get('book-names'), 
                    type=request.form.get('type'), cost =request.form.get('cost'),
                    quantity= request.form.get('quantity'),executedqty=0,status='PLACED',orderdate='29-01-2022')
            db.session.add(order)
            print(order)
            db.session.commit()
            flash('books added','success')
            return render_template('customer.html')


@app.route('/admin',methods=['POST','GET'])
def admin():
    return render_template("admin.html",orders=orders.query.all())

@app.route('/sample')
def sample():
    
    return render_template("sample.html")

class database(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

def _init_(self,email,password):
    self.email=email
    self.password=password

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
        DB=database(email=request.form.get('email'),password = request.form.get('password'))
        db.session.add(DB)
        db.session.commit()
        flash('registered','success')
    return render_template("register.html")


@app.route('/login',methods=['POST','GET'])
def login():
    email=request.form.get('email')
    password=request.form.get('password')
    d = database.query.filter_by(email=email).first()
    if not d :
        flash('please check details')
        return render_template("login.html",database=database)
    else:
        flash('welcome')
        redirect(url_for('customer'))

    return render_template("login.html",database=database)

@app.route('/c',methods=['POST','GET'])
def closed():
        return render_template('closed.html')

if __name__== '__main__':
    
    db.create_all()
    app.run(debug=True)
    session['open']='1'
    