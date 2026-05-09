from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
import secrets
from functools import wraps

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



db= SQLAlchemy(app)


class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    password_hash=db.Column(db.String(255),nullable=False)
    token=db.Column(db.String(255),unique=True,index=True)


    def set_token(self):
        self.token=secrets.token_hex(32)
        print(self.token)

class Category(db.Model):
    __tablename__="category"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)


#Expense (id, title, amount, date, user_id → User, category_id → Category)


class Expense(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    amount=db.Column(db.Integer,nullable=False)
    date=db.Column(db.String(100),nullable=False)
    user_id=db.Column(db.Integer,ForeignKey('user.id'),nullable=False)
    category_id=db.Column(db.Integer,ForeignKey('category.id'),nullable=False)


with app.app_context():
    db.create_all()



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith("Bearer"):
            return jsonify({"message":"invalid token "})
        token=token.split()[1]
        user = User.query.filter(User.token==token).first()
        print(user)
        if not user:
            return jsonify({'message': 'Unauthorized'})
        return f(*args, **kwargs, current_user=user)
     
    return decorated

@app.route('/api/login',methods={'POST'})
def login():
    data=request.get_json()
    users=User.query.filter(User.user_name==data["user_name"]).first()
    if users and users.password_hash==data["password_hash"]:
        users.set_token()
        db.session.commit()
        return jsonify({"token":users.token})
    return jsonify({"message":"invalid username or password"})

   



#GET,POST,PUT,DELETE QUERY FOR USER TABLE

@app.route('/api/alluser',methods=["GET"])
@token_required
def all_user(current_user):
    users=[{
        "id":value.id,
        "user_name":value.user_name,
        "email":value.email,
        "password_hash":value.password_hash

    }for value in(User.query.all())
    ]
    return jsonify(users)



@app.route('/api/getuser/<int:id>',methods=["GET"])
@token_required
def get_user(id,current_user):
    users=[
        {   "id":value.id,
            "user_name":value.user_name,
            "email":value.email,
            "password_hash":value.password_hash
        }for value in(User.query.filter(User.id==id))]
    
    if users:
        return jsonify(users)
    return jsonify({"message":"user not found"})
    



@app.route('/api/postuser',methods=["POST"])
@token_required
def post_users(current_user):
    data=request.get_json()
    new_user=User(user_name=data["user_name"],email=data["email"],password_hash=data["password_hash"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"new user created"})

@app.route('/api/putuser/<int:id>',methods=["PUT"])
@token_required
def update_users(id,current_user):
    data=request.get_json()
    users=User.query.get(id)
    if users:
        users.user_name=data.get('user_name',users.user_name)
        users.email=data.get('email',users.email)
        users.password_hash=data.get('password_hash',users.password_hash)
        db.session.commit()
        return jsonify({"message":"user updated"})
    return jsonify({"message":"not found"})


@app.route('/api/deleteuser/<int:id>',methods=["DELETE"])
@token_required
def delete_user(id,current_user):
    users=User.query.get(id)
    if users:
        db.session.delete(users)
        db.session.commit()
        return jsonify({"message":"Deletion Successful"})
    return jsonify({'message':"deleted successfully"})


#GET,POST,PUT,DELETE QUERY FOR CATEGORY TABLE


@app.route('/api/allcategory',methods=["GET"])
@token_required
def all_category(current_user):
    allcat=[{
        "id":value.id,
        "name":value.name
        

    }for value in(Category.query.all())
    ]
    return jsonify(allcat)


@app.route('/api/cat/<int:id>',methods=["GET"])
@token_required
def get_catbyid(id,current_user):
    cate=[{
        "id":value.id,
        "name":value.name
       
    }for value in(Category.query.filter(Category.id==id))]
    if cate:
        return jsonify(cate)
    
    return jsonify({"message":"not found"})



@app.route('/api/postcat',methods=["POST"])
@token_required
def post_category(current_user):
    data=request.get_json()
    new_category=Category(name=data["name"])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message":"new category added"})






@app.route('/api/putcat/<int:id>',methods=["PUT"])
@token_required
def update_cat(id,current_user):
    data=request.get_json()
    cate=Category.query.get(id)
    if cate:
        cate.name=data.get('user_name',cate.name)
        db.session.commit()
        return jsonify({"message":"category updated"})
    return jsonify({"message":"not found"})


@app.route('/api/deletecat/<int:id>',methods=["DELETE"])
@token_required
def delete_category(id,current_user):
    cate=Category.query.get(id)
    if cate:
        db.session.delete(cate)
        db.session.commit()
        return jsonify({"message":"category deleted"})
    return jsonify({"message":"deleted successfully"})


#GET,POST,PUT,DELETE QUERY FOR EXPENSE TABLE


            

@app.route('/api/getexp',methods=["GET"])
@token_required
def get_exp(current_user):
    expenses=[{
        "id":value.id,
        "title":value.title,
        "amount":value.amount,
        "date":value.date,
        "user_id":value.user_id,
        "category_id":value.category_id,

    }for value in(Expense.query.all())
    ]
    return jsonify(expenses)



@app.route('/api/postexp',methods=["POST"])
@token_required
def create_exp(current_user):
    data=request.get_json()
    new_exp=Expense(title=data["title"],amount=data["amount"],date=data["date"],user_id=data["user_id"],category_id=data["category_id"])
    db.session.add(new_exp)
    db.session.commit()
    return jsonify({"message":"successful addition of new expense"})



@app.route('/api/updateexp,<int:id>',methods={"PUT"})
@token_required
def update_expenses(id,current_user):
    data=request.get_json()
    new_expenses=Expense.query.get(id)
    if new_expenses:
        new_expenses.title=data.get("title",new_expenses.title)
        new_expenses.amount=data.get("amount",new_expenses.amount)
        new_expenses.date=data.get("date",new_expenses.date)
        db.session.add(new_expenses)
        db.session.commit()
        return jsonify({"message":"expense updated"})
    return jsonify({"message":"not found"})
    


@app.route('/api/deleteexp/<int:id>',methods=["DELETE"])
@token_required
def delete_expense(id,current_user):
    exp=Expense.query.get(id)
    if exp:
        db.session.delete(exp)
        db.session.commit()
        return jsonify({"message":"expense deleted"})
    return jsonify({"message":"deleted successfully"})



@app.route('/api/getexpcat',methods=["GET"])
@token_required
def get_spescificcat(current_user):
    expenses=[{
        "title":value.title,
        "amount":value.amount,
        "date":value.date,
        "user_id":value.user_id,
        "name":value.name,
        "category_id":value.category_id

    }for value in(db.session.query(Expense.title,Expense.amount,Expense.date,Expense.user_id,Expense.category_id,Category.name).join(Category,Category.id==Expense.category_id)).all()
    ]
    return (expenses)

@app.route('/api/getexpname/<string:name>',methods=["GET"])
@token_required
def getexp_bycatname(name,current_user):
    expense=[{
        "title":value.title,
        "amount":value.amount,
        "date":value.date,
        "user_id":value.user_id,
        "name":value.name,
        "category_id":value.category_id,
        "user_name":value.user_name
    }for value in(db.session.query(Expense.title,Expense.amount,Expense.date,Expense.user_id,Expense.category_id,Category.name,User.user_name).join(Category,Category.id==Expense.category_id)).join(User,User.id==Expense.user_id).filter(Category.name==name)]
    if expense:
        return jsonify(expense)
    return jsonify({"message":"error"})




@app.route('/api/logout',methods=["GET"])
@token_required
def logout(current_user):
    current_user.token=None
    db.session.commit()
    return jsonify({"message":"logout successful"})



if __name__=="__main__":
    app.run(debug=True)





