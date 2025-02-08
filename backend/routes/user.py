from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.route("/preferences", methods=["GET", "POST"])
def user_preferences():
    return jsonify({"message": "User preferences feature is not implemented yet."})
