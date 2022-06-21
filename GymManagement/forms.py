from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import configure_uploads, IMAGES, UploadSet
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms.fields import DateField,DateTimeField 
from GymManagement.models import Trainer,Member

class AddMemberForm(FlaskForm):

    def validate_member(self, name_to_check):
        member = Member.query.filter_by(name=name_to_check.data).first()
        if user:
             raise ValidationError('Member already exists! Please try a different name')
    def validate_email_address(self, email_address_to_check):
        email_address = Member.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(('Member already exists! Please use a differnt Email Address '))         
    
    name = StringField(label='User Name:', validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    phonenumber = IntegerField(label='Phone Number: ',validators=[DataRequired()])
    myChoices = ['Male', 'Female', 'Unspecified']
    gender = SelectField(label='Gender',choices = myChoices, validators=[DataRequired()])
    dob = DateField(label = 'Date of birth', format='%Y-%m-%d', validators=[DataRequired()])
    regdate = DateField(label = 'Registration date', format='%Y-%m-%d', validators=[DataRequired()])
    membershipdate = DateField(label = 'Membership Availability date', format='%Y-%m-%d', validators=[DataRequired()])
    address = StringField(label='Address', validators=[DataRequired()])
    image_1 = FileField(label='image')
    submit = SubmitField(label='Add Patient')


class AddTrainerForm(FlaskForm):

    def validate_member(self, name_to_check):
        trainer = Trainer.query.filter_by(name=name_to_check.data).first()
        if user:
             raise ValidationError('Member already exists! Please try a different name')
    def validate_email_address(self, email_address_to_check):
        email_address = Trainer.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(('Member already exists! Please use a differnt Email Address '))         
    
    name = StringField(label='User Name:', validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    phonenumber = IntegerField(label='Phone Number: ',validators=[DataRequired()])
    myChoices = ['Male', 'Female', 'Unspecified']
    gender = SelectField(label='Gender',choices = myChoices, validators=[DataRequired()])
    dob = DateField(label = 'Date of birth', format='%Y-%m-%d', validators=[DataRequired()])
    regdate = DateField(label = 'Registration date', format='%Y-%m-%d', validators=[DataRequired()])
    address = StringField(label='Address', validators=[DataRequired()])
    image_1 = FileField(label='image')
    submit = SubmitField(label='Add Patient')    