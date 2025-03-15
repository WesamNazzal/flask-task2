from flask import Flask, Response, jsonify

from presentation.exceptions.app_exception import AppException
from presentation.routes.app_route.app_route import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True


@app.errorhandler(AppException)
def handle_app_exception(error: AppException) -> Response:
    response = jsonify(error.to_dict())
    response.status_code = error.code if error.code is not None else 500
    return response


@app.errorhandler(Exception)
def handle_generic_exception(error: Exception) -> Response:
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response


app.run(debug=True)
