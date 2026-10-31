from flask import Blueprint, render_template

from models import Report
from extensions import db

list_items_bp = Blueprint("list_items", __name__)


@list_items_bp.route("/")
def list_items():
    reports = (
        db.session.execute(db.select(Report).order_by(Report.id.desc())).scalars().all()
    )

    return render_template("list_items.html", reports=reports)
