from unbabel import create_app


def test_config():
    assert not create_app(False).testing
    assert not create_app(False).debug
    assert create_app(True).testing
