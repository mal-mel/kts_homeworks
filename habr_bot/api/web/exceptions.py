class Error(Exception):
    status = 500
    code = "internal_error"
    description = "Internal Server Error"

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "code": self.code,
            "description": self.description
        }


class AlreadyExists(Error):
    status = 400
    code = "already_exists"
    description = "Object already exists"


class InvalidCredentials(Error):
    status = 400
    code = "invalid_credentials"
    description = "Credentials data is invalid"


class NotFound(Error):
    status = 404
    code = "not found"
    description = "Object not found"


class NotAuthorized(Error):
    status = 401
    code = "not_authorized"
    description = "Not Authorized"
