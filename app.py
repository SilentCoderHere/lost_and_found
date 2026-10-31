from flask import Flask
from routes.home import home_bp
from routes.list_items import list_items_bp
from routes.report import report_bp
from extensions import db

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(report_bp, url_prefix="/report")
app.register_blueprint(list_items_bp, url_prefix="/list-items")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lost_found.db"
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
    )
