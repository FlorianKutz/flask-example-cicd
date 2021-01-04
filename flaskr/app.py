from flask import Flask, render_template
from . import prime_cython as pc

app = Flask(__name__)

hello_message = "This is a message from flask!"


@app.route('/')
def index():
    return render_template("index.html", message=hello_message)


@app.route('/json/')
def json():
    return {"hello": "world2"}


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = "Anonymous"
    return render_template("hello.html", name=name)

@app.route('/hello/random')
def hello_random():
    return render_template("hello.html", name="Todo")


@app.route('/primes/')
@app.route('/primes/<int:count>')
def primes(count=None):
    if count is None or count == 0:
        return render_template("primes.html")
    elif count > 1000:
        return "Please select a natural number lower or equal to 1000."
    # Return prime.html with list of prime numbers
    return render_template("primes.html", count=str(count),
                           primes=str(pc.primes(count)))


# Debug flask app - if run as main application
# To run this application use "python -m flaskr.app" from the project root folder
if __name__ == '__main__':
    app.env = "development"
    app.run(debug=True, host='0.0.0.0', port=8080)
