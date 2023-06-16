from flask import Flask
app = Flask(__name__)

@app.route('/hello/<int:numero>')
def show_blog(numero):
   return 'Blog Number %d' % 134

@app.route('/hello/<float:decimale>')
def revision(decimale):
   return 'Revision Number %f' % 1.1

if __name__ == '__main__':
   app.run()