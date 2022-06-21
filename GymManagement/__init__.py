from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_uploads import configure_uploads, IMAGES, UploadSet, patch_request_class
import os

basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym.db'
app.config['SECRET_KEY'] = 'b21dc07d19eba5e6f64f026f'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
# photos = UploadSet('photos', '', IMAGES) // this allows emptyu files to be stored but gives error when storing photo



configure_uploads(app, photos)
patch_request_class(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view="login_page"
# login_manager.login_message_category = "info"
from GymManagement import routes


#import from HospitalManagment se karna hai