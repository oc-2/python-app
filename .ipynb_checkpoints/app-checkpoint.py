import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import CSRFProtect
from forms import ContactForm
# from flask_sqlalchemy import SQLAlchemy
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
csrf = CSRFProtect(app)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/app'

# db=SQLAlchemy(app)

# class Student(db.Model):
  # __tablename__='app'
  # id=db.Column(db.Integer,primary_key=True)
  # fname=db.Column(db.String(40))
  # lname=db.Column(db.String(40))
  # pet=db.Column(db.String(40))

  # def __init__(self,fname,lname,pet):
  #  self.fname=fname
  #  self.lname=lname
  #  self.pet=pet

@app.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real application, you would process the form data here
        # For now, we'll just show a success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('index'))
    
    flash('There was an error with your submission. Please try again.', 'error')
    return redirect(url_for('index'))
