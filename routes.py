from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    name=name.title()
    return 'Hi '+name+'!'
@app.route('/repeat/<int:num>/<string>')
def repeat(num, string):
    string+=" "
    return string*num
@app.errorhandler(404)
def pageNotFound(e):
    return "Though we looked everywhere, our team of highly trained monkey has not yet created this page. Please try a different web address."

if __name__=='__main__':
    app.run(debug=True)