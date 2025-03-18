
from flask import Blueprint, Response, jsonify, request
from flask.views import MethodView

from application.services.book_service import BookService
from presentation.exceptions.app_exception import AppException

book_bp = Blueprint('books', __name__)
book_service = BookService()


class BookAPI(MethodView):
    def get(self, book_id: int | None = None) -> tuple[Response, int]:
        try:
            if book_id is None:
                books, status = book_service.get_all()
                return jsonify(books), status if status is not None else 500

            book, status = book_service.get_book_by_id(book_id)
            return jsonify(book), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_borrowed_book(self, book_id: int) -> tuple[Response, int]:
        try:
            book_info, status = book_service.get_borrowed_book_with_member(book_id)
            return jsonify(book_info), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def post(self) -> tuple[Response, int]:
        try:
            data = request.get_json()
            book, status = book_service.create(data)
            return jsonify(book), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def patch(self, book_id: int) -> tuple[Response, int]:
        try:
            data = request.get_json()
            book, status = book_service.update_book(book_id, data)
            return jsonify(book), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete(self, book_id: int) -> tuple[Response, int]:
        try:
            response, status = book_service.delete_book(book_id)
            return jsonify(response), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500


class BorrowReturnAPI(MethodView):
    def post(self, book_id: int, member_id: int) -> tuple[Response, int]:
        try:
            book, status = book_service.borrow_book(book_id, member_id)
            return jsonify(book), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def put(self, book_id: int) -> tuple[Response, int]:
        try:
            book, status = book_service.return_book(book_id)
            return jsonify(book), status if status is not None else 500

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500


book_view = BookAPI.as_view('book_api')
borrow_return_view = BorrowReturnAPI.as_view('borrow_return_api')

book_bp.add_url_rule('/', view_func=book_view, methods=['POST', 'GET'])
book_bp.add_url_rule('/<int:book_id>', view_func=book_view, methods=['GET', 'PATCH', 'DELETE'])
book_bp.add_url_rule('/borrow/<int:book_id>/<int:member_id>', view_func=borrow_return_view, methods=['POST'])
book_bp.add_url_rule('/return/<int:book_id>', view_func=borrow_return_view, methods=['PUT'])
book_bp.add_url_rule('/borrowed/<int:book_id>', view_func=book_view, methods=['GET'])
