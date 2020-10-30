from flask import Flask, render_template, request
from send_email import send_email
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/horoscope", methods=["POST"])
def horoscope():
    if request.method=='POST':
        sign=request.form['signs']
        email=request.form['user_email']
        (status,lst)=send_email(email,sign)
        print(sign,sep="\n")
    if status:
        return render_template("success.html",yes=lst[0],tom=lst[2])
    return render_template("index.html",text="Enter valid Zodiac sign")


if __name__=="__main__":
    app.debug=True
    app.run() 