from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from cqrs_template.authentication import authentication
app.register_blueprint(authentication, url_prefix="/auth")

from cqrs_template.module2 import module2
app.register_blueprint(module2)

if __name__ == "__main__":
    app.run()