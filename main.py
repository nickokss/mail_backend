from flask import Flask
from app import views

app = Flask(__name__)

# Registro de rutas
app.register_blueprint(views.email_bp)

if __name__ == '__main__':
    app.run(debug=True)
