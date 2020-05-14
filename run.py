"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 2/12/18

"""

from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1'

posts = []


@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return render_template("index.html", num_posts=len(posts))


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)