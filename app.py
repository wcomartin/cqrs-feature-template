from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


from cqrs_template.authentication import authentication

app.register_blueprint(authentication, url_prefix="/auth")

if __name__ == "__main__":
    app.run()
