from flask import Flask

app = Flask(__name__)  # creating the Flask class object


@app.route('/hello')  # decorator drfines the
def home():
    return "Ciao, sono hello";


if __name__ == '__main__':
    app.run(debug=True)