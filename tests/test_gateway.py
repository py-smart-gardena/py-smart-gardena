from gardena.gateway import Gateway
import pytest


def test_init():
    gw = Gateway(email='test@test.com', password='password')
    assert gw.email == 'test@test.com'
    assert gw.password == 'password'


def test_init_exception_without_email():
    with pytest.raises(ValueError):
        gw = Gateway(password='password')


def test_init_exception_without_password():
    with pytest.raises(ValueError):
        gw = Gateway(email='test@test.com')
