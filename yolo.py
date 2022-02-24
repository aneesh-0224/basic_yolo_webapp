from flask import Flask, render_template, redirect, url_for,request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField
import os

app=Flask(__name__)
app.config['SECRET_KEY']='568325235'

class imgForm(FlaskForm):
    p_img = FileField(label='Image',validators=[FileAllowed(['jpeg','png'])])
    submit = SubmitField(label='Submit')

def save_img(pic):
    picture_name='target.jpeg' or pic.filename
    picture_path=os.path.join(app.root_path,'static/input',picture_name)
    pic.save(picture_path)
    return picture_name

@app.route('/',methods=['GET','POST'])
def home_page():
    form = imgForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        img_file_name=save_img(form.p_img.data)
        #Since after calling the save_img function the the image is stored in static/input it can be used
        #as input for the model and the model can be instantiated here.and the output of the model can be 
        #put in the static/output folder.
        print(app.root_path)
        return render_template('show.html',path=app.root_path)
    return render_template('homepage.html',form=form)


