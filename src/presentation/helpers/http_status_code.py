import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class HttpStatusCode:
    OK: int = 200
    CREATED: int = 201
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401
    INTERNAL_SERVER_ERROR: int = 500