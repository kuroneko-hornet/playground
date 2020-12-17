from flask import Flask ,render_template,request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/sample',methods=['POST'])
def sample():
    message = request.form['message']
    return render_template('post.html',message=message)

if __name__=="__main__":
    application.run(host='0.0.0.0')

