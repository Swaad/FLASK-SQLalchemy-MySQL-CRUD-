from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:root#1234@localhost/credit_scoring'
db = SQLAlchemy(app)
#db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# engine = create_engine('mysql+mysqlconnector://root:root#1234@localhost/test_scoring', echo=False)

@app.route("/asd", methods=["GET", "POST"])
def asd():
    try:
        if request.method == 'POST':
            json_data = request.get_json()
            username = json_data["user_name"]
            email = json_data["email"]
            print(username)
            print(email)


        print("API Has been hit")
        return jsonify(
            {"message": "Hello", "severity": "danger"}
        )
    except Exception as e:
        print(e)
        return jsonify(
            {"message": "Hello", "severity": "danger"}
        )



@app.route('/post', methods=["GET", "POST"])
def hello_world():
    # put application's code here
    try:
        json_data = request.get_json()
        username = json_data["user_name"]
        email = json_data["email"]
        print(username)
        print(email)
        # db.create_all()
        # db.session.add(username)
        # db.session.commit()
        todo = Customers(username=username, email=email)
        db.session.add(todo)
        db.session.commit()
        Customers.query.all()
        # customers.read_by_id(1)
        # customers.update_data("Neon", "Neon_rocks also mainul")
        # read_all = customers.read_all()
        return "row added done"
    except Exception as e:
        print(e)
        return str(e)

@app.route("/delete/<int:id>")
def delete(id):
        deletetodo = Customers.query.filter_by(id=id).first()
        db.session.delete(deletetodo)
        db.session.commit()
        return "Deleted row"

@app.route("/updatetodo/<int:id>",methods=['POST'])
def update_todo(id):
    try:
        if request.method == 'POST':
            updatetodo = Customers.query.filter_by(id=id).first()
            json_data = request.get_json()
            username = json_data["user_name"]
            email = json_data["email"]
            print(username)
            print(email)
            print(updatetodo)
            todo = Customers(username=username, email=email)
            updatetodo.username = username
            updatetodo.email = email
            db.session.commit()
            return "Updated done"
        # updatetodo = Customers.query.filter_by(id=id).first()
        # return "Updated row"
    except Exception as e:
        print(e)
        return str(e)




class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    # def __init__(self, username, email):
    #     db.create_all()
    #     db.session.add(username)
    #     db.session.commit()
        # self.username = username
        # self.email = email

    # def add_data(self, username=None, email=None):
    #     # chat_log = Customers(username, email)
    #     db.session.add(username)
    #     db.session.add(email)
    #     db.session.commit()
    #     db.session.close()
    #     db.session.remove()
    #     db.engine.dispose()

    def read_by_id(self, id):
        chat_history_by_id = Customers.query.filter_by(id=id).first()
        return chat_history_by_id

    def read_all(self):
        all_data = Customers.query.all()
        return all_data

    # def update_data(self, filter_by_email_value, update_value):
    #     update_this = Customers.query.filter_by(email=filter_by_email_value).first()
    #     update_this.mobile_number = update_value
    #     db.session.commit()
    #     db.session.close()
    #     db.session.remove()
    #     db.engine.dispose()
    #
    # def delete_data(self, value):
    #     delete_this = Customers.query.filter_by(username=value).first()
    #     db.session.delete(delete_this)
    #     db.session.commit()
    #     db.session.close()
    #     db.engine.dispose()


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
