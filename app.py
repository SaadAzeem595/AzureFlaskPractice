from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This matches the sample in image_3.png
    return '<h1>Hello from Azure Flask Practice!</h1><p>Continuous deployment is working.</p>'

if __name__ == '__main__':
    # When running locally, start the test server
    app.run()