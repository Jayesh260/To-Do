from flask import Flask,render_template ,request,redirect,url_for

app=Flask(__name__,template_folder= 'templates')      
#creating an instance of the class Flask

todo=[]                              #list to store all tasks 


@app.route('/')
#defining a route  for the index page 
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)
    