from extensions import db


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(10), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(150), nullable=False)
    item_date = db.Column(db.String(20))
    photo_path = db.Column(db.String(255))
    contact_info = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), default="open")
