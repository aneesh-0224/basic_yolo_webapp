from urllib import request
from flask import Flask, render_template, redirect, url_for,request
import matplotlib.pyplot as plt
app=Flask(__name__)
s_img_path=None
@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/newimg',methods=['POST'])
def new_img():
    s_img_path = request.form.get('s_img')
    print(s_img_path)
    s_img = plt.imread('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/data' + '/' +s_img_path)
    # Here we get the image required for our model.
    #So now we will put the image in a input folder from where the model will take the image.
    temp=plt.imshow(s_img)
    plt.savefig('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/inputs/'+s_img_path)
    #After this we use the model to perform the task and output the result in an output folder and then 
    # display on to the screen whatever the output folder has.
    plt.savefig('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/outputs/'+'r1.jpeg') #temporary code
    return redirect('/show')

@app.route('/show')
def show_img():
    return render_template('show.html',name=s_img_path,fixed_path='C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/outputs/')
    

