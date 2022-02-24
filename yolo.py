from flask import Flask, render_template, redirect, url_for,request
import matplotlib.pyplot as plt
import json
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField
import os
app=Flask(__name__)
app.config['SECRET_KEY']='568325235'
s_img_path=None
class imgForm(FlaskForm):
    p_img = FileField(label='Image',validators=[FileAllowed(['jpeg','png'])])
    submit = SubmitField(label='Submit')

def save_img(pic):
    picture_name=pic.filename
    print(app.root_path)
    picture_path=os.path.join(app.root_path,'static/inputs',picture_name)
    pic.save(picture_path)
    return picture_name

@app.route('/',methods=['GET','POST'])
def home_page():
    form = imgForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.p_img.data)
        img_file=save_img(form.p_img.data)
        return redirect('/')
    return render_template('home.html',form=form)
    #return render_template('homepage.html')

#@app.route('/newimg',methods=['POST'])
#def new_img():
    #s_img_path = request.form.get('s_img')
    #s_img = plt.imread('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/data' + '/' +s_img_path)
    # Here we get the image required for our model.
    #So now we will put the image in a input folder from where the model will take the image.
    #temp=plt.imshow(s_img)
    #plt.savefig('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/inputs/'+s_img_path)
    #After this we use the model to perform the task and output the result in an output folder and then 
    # display on to the screen whatever the output folder has.
    #plt.savefig('C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/outputs/'+'r1.jpeg') #temporary code
    #return redirect('/show')

@app.route('/show')
def show_img():
    return render_template('show.html',name=s_img_path,fixed_path='C:/Users/Aneesh Kulkarni/web_dev/flask projects/web page for yolo/outputs/')
    

