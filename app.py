from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hey yo'

@app.route('/about')
def about():
    return 'ABOUT'
# if __name__=="__main__":
#     app.run(debug=True)