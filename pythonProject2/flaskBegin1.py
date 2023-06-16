from flask import Flask
app = Flask(__name__)

@app.route('/hello/<ciaoMondo>')
def hello_name(ciaoMondo):
   return 'Hello' "carlo"

if __name__ == '__main__':
   app.run(debug = True)