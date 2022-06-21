from flask import render_template, redirect, url_for, flash, request
from GymManagement.models import Trainer, Member
from GymManagement import app
from GymManagement.forms import AddMemberForm,AddTrainerForm
from GymManagement import db,app,photos
import secrets

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
    
@app.route( '/member', methods=['GET','POST'])
def member_page():
    members = Member.query.all()
    return render_template('member.html', members=members)
@app.route( '/Trainer', methods=['GET','POST'])
def trainer_page():
    trainers = Trainer.query.all()
    return render_template('Trainer.html', trainers=trainers)

@app.route('/addMember', methods=['GET', 'POST'])    
def addMember():
    form = AddMemberForm()
    if form.validate_on_submit():
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        add_Member = Member(name=form.name.data, email_address = form.email_address.data, phonenumber=form.phonenumber.data, gender=form.gender.data, dob = form.dob.data, regdate = form.regdate.data,
        membership_available = form.membershipdate.data ,address = form.address.data, img = image_1 )
        db.session.add(add_Member)
        db.session.commit()

        flash(f'The Patient {form.name.data} has been added!', 'success')
        return redirect(url_for("member_page"))

    return render_template('addMember.html', form=form)


@app.route('/addTrainer', methods=['GET', 'POST'])    
def addTrainer():
    form = AddTrainerForm()
    if form.validate_on_submit():
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        add_Trainer = Trainer(name=form.name.data, email_address = form.email_address.data, phonenumber=form.phonenumber.data, gender=form.gender.data, dob = form.dob.data, regdate = form.regdate.data,address = form.address.data, img = image_1 )
        db.session.add(add_Trainer)
        db.session.commit()

        flash(f'The Trainer {form.name.data} has been added!', 'success')
        return redirect(url_for("Trainer_page"))

    return render_template('addTrainer.html', form=form)
