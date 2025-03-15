from flask import Blueprint, jsonify, request
from flask.views import MethodView

from application.services.member_service import MemberService
from presentation.exceptions.app_exception import AppException

member_bp = Blueprint('members', __name__)
member_service = MemberService()


class MemberAPI(MethodView):
    def get(self, member_id: int = None):
        try:
            if member_id is None:
                members, status = member_service.get_all()
                return jsonify(members), status
            
            member, status = member_service.get_by_id(member_id)
            return jsonify(member), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def post(self):
        try:
            data = request.get_json()
            member, status = member_service.create_member(data)
            return jsonify(member), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def put(self, member_id: int):
        try:
            data = request.get_json()
            member, status = member_service.update_member(member_id, data)  
            return jsonify(member), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete(self, member_id: int):
        try:
            _, status = member_service.delete_member(member_id)  
            return jsonify({'message': 'Member deleted successfully!'}), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500


class MemberSearchAPI(MethodView):
    def get(self, email: str):
        try:
            member, status = member_service.get_member_by_email(email)
            return jsonify(member), status

        except AppException as e:
            return jsonify(e.to_dict()), e.code
        except Exception as e:
            return jsonify({'error': str(e)}), 500


member_view = MemberAPI.as_view('member_api')
member_search_view = MemberSearchAPI.as_view('member_search_api')

member_bp.add_url_rule('/', view_func=member_view, methods=['POST', 'GET'])
member_bp.add_url_rule('/<int:member_id>', view_func=member_view, methods=['GET', 'PUT', 'DELETE'])  # ✅ Fixed type
member_bp.add_url_rule('/email/<string:email>', view_func=member_search_view, methods=['GET'])
