from flask import Flask , render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def main_route():
    name="Ali"
    return render_template("index.html", name=name)

@app.route("/download")
def download():
    media=["1","2","3"]
    return render_template("download.html", media=media )

@app.route("/blog", methods=["GET", "POST"])
def my_blog():
    if request.method == "GET":
        return "this is GET method"    
    elif request.method == "POST":
        return "this is POST method"
