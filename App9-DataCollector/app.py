from flask  import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sherlock@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)


    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("dataCollector-Frontend.html")

@app.route("/success", methods=['POST']) 
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height"]
        print(email, height)
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height, 1)
            count=db.session.query(Data.height_).count()
            print(" Avg height : %s out of %s number of people " % (str(average_height), count) )
            return render_template("success.html")
    return render_template("dataCollector-Frontend.html", text="Email already exists, Please try with new Email ID!!!")

if __name__=="__main__":
    app.run(debug=True)e