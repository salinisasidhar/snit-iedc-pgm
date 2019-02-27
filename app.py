from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>hello...</h1>"
@app.route("/home")
def home():
    return "Welcome to my home page"
@app.route("/about")
def about():
    return "About as page"
@app.route("/contact")
def contact():
    return "Contact Us page"
if(__name__=="__main__"):
    app.run(debug=True)
