from werkzeug.exceptions import HTTPException


class AppException(HTTPException):

    def __init__(self, message: str, status_code: int):
        super().__init__(description=message)
        self.message = message
        self.code = status_code

    def to_dict(self) -> dict[str, str]:
        return {'error': self.message}
