import os
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "commentdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
class Comment(db.Model):
    webblog = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Webblog: {}>".format(self.webblog)

@app.route("/", methods=["GET", "POST"])

def home():
    comments = None
    if request.form:
        try:
            comment = Comment(webblog=request.form.get("webblog"))
            db.session.add(comment)
            db.session.commit()
        except Exception as e:
            print("Failed to add comment")
            print(e)
    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

@app.route("/update", methods=["POST"])
def update():
    try:
        newwebblog = request.form.get("newwebblog")
        oldwebblog = request.form.get("oldwebblog")
        comment = Comment.query.filter_by(webblog=oldwebblog).first()
        comment.webblog = newwebblog
        db.session.commit()
    except Exception as e:
        print("Couldn't update comment webblog")
        print(e)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
