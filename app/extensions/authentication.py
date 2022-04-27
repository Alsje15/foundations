from flask_login import LoginManager
from app.routes.models import Chef

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return Chef.query.get(int(user_id))
    