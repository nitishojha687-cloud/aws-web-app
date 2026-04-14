from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello AWS Deployment 🚀"

# IMPORTANT for AWS
application = app

if __name__ == "__main__":
    app.run()