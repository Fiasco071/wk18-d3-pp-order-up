from flask import Flask
from flask_login import LoginManager
from app.config import Configuration
from app.routes import orders, session
from app.models import db, Employee


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)
db.init_app(app)

login = LoginManager(app)
login.login_view = "session.login"

@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
