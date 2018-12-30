from gardena.gateway import Gateway


def test_init():
    gw = Gateway(email='test@test.com', password='password')
    assert gw.email == 'test@test.com'
    assert gw.password == 'password'