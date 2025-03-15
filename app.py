from flask import Flask, jsonify

from presentation.exceptions.app_exception import AppException
from presentation.routes.app_route.app_route import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

app.config['PROPAGATE_EXCEPTIONS'] = True  
app.config['DEBUG'] = True

@app.errorhandler(AppException)
def handle_app_exception(error: AppException):
    response = jsonify(error.to_dict())
    response.status_code = error.code
    return response

@app.errorhandler(Exception)
def handle_generic_exception(error):
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response

if __name__ == "__main__":
    app.run(debug=True)
