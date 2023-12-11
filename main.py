from flask import Flask
from routes.user_routes import form_bp
import config

app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
app.register_blueprint(form_bp)


if __name__ == '__main__':
    app.run(debug=True)
