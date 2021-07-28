from flask import Flask,render_template,request
from main import firebase
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/view',methods=['POST','GET'])
def retriveData():
    try:
        if request.method=="GET":
            filename=request.args.get('id')
            print(filename)


            storage=firebase.storage()

            #upload=input('enter the file name')
            # as admin

            #storage.child("pdf/"+upload+'.pdf').put('static/pdf/'+upload+'.pdf')
            # as user

            url=storage.child("pdf/"+filename+".pdf").get_url(None)
            # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images%2Fexample.jpg?alt=media

        return render_template('index.html',Url=url)
    except:
        print()

if __name__ == '__main__':
    app.run()
