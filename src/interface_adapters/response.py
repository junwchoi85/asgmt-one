from typing import Any, Optional


class Response:
    def __init__(self, status_code: str, message: str, data: Optional[Any] = None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "statusCode": self.status_code,
            "message": self.message,
            "data": self.data
        }
