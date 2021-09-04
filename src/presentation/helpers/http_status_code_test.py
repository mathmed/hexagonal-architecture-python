from .http_status_code import HttpStatusCode

sut = HttpStatusCode()

def test_should_confirm_correct_http_status():
    assert sut.OK == 200
    assert sut.CREATED == 201
    assert sut.BAD_REQUEST == 400
    assert sut.UNAUTHORIZED == 401
    assert sut.INTERNAL_SERVER_ERROR == 500
