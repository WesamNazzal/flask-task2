from flask import Blueprint

from presentation.routes.book_route import book_bp
from presentation.routes.member_route import member_bp

main_bp = Blueprint('main', __name__)

main_bp.register_blueprint(book_bp, url_prefix='/books')
main_bp.register_blueprint(member_bp, url_prefix='/members')
