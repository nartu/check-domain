"""
app tests example

"""

from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com')


def test_down():
    assert not is_alive_host('invalid.domain.son')
