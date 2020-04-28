from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/<page_name>')
def route1(page_name):
    return render_template(page_name)


@app.route('/')
def route0():
    return render_template("index.html")


@app.route('/submit_data', methods=['GET', 'POST'])
def submit_data():
    data = request.form.to_dict()
    email = data.get("email")
    text = data.get("text")
    subject = data.get("subject")
    print(email)
    return render_template("/thankyou.html", email=email, text=text, subject=subject)
# @app.route('/index.html')
# def route2():
#     return render_template('index.html')
#
#
# @app.route('/works.html')
# def route3():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def route4():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def route5():
#     return render_template('contact.html')
