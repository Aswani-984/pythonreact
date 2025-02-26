from flask import Blueprint, request, jsonify, current_app
from app.models import db, User
from flask_mail import Message
from app import mail


main = Blueprint("main", __name__)

@main.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    # Save to Database
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    # Send Email Notification
    msg = Message("Registration Successful", sender=current_app.config["MAIL_USERNAME"], recipients=[email])
    msg.body = f"Hello {name},\n\nYou have successfully registered!\n\nThank you."
    mail.send(msg)

    return jsonify({"message": "User registered and email sent successfully!"}), 201
