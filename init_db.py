from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all() 
    admin_user = User(username='admin', password=generate_password_hash('admin_password'), is_admin=True)
    db.session.add(admin_user)
    db.session.commit()
