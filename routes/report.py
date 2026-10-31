from os import makedirs, path
from uuid import uuid4

from flask import Blueprint, current_app, redirect, render_template, request, url_for
from werkzeug import Response
from models import Report
from extensions import db

report_bp = Blueprint("report", __name__)


@report_bp.route("/", methods=["GET", "POST"])
def report() -> Response | str | tuple[str, int]:
    if request.method == "POST":
        photo = request.files.get("photo")
        photo_path = None

        if photo and photo.filename:
            splits = photo.filename.split(".")
            file_extension = splits[-1].lower()

            if len(splits) == 1:
                return "Invalid photo file", 400

            if not file_extension in {"jpeg", "jpg", "png", "webp"}:
                return "Invalid file extension", 400

            upload_folder = path.join(
                current_app.static_folder if current_app.static_folder else "static",
                "uploads",
            )
            makedirs(upload_folder, exist_ok=True)

            filename = f"{uuid4().hex}.{file_extension}"
            photo.save(path.join(upload_folder, filename))
            photo_path = f"uploads/{filename}"

        new_report = Report(
            report_type=request.form.get("report_type"),
            item_name=request.form.get("item_name"),
            category=request.form.get("category"),
            description=request.form.get("description"),
            location=request.form.get("location"),
            item_date=request.form.get("item_date"),
            photo_path=photo_path,
            contact_info=request.form.get("contact_info"),
        )

        db.session.add(new_report)
        db.session.commit()

        return redirect(url_for("report.report"))

    return render_template("report.html")
