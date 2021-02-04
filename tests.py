"""
app tests example

"""
import pytest
from app import is_alive_host

# def test_alive_host():
#     assert is_alive_host('ya.ru') == 'on'
#
#
# def test_down_host():
#     assert is_alive_host('102.com') == 'off'


@pytest.mark.parametrize(
    ('hostname','answer'),
    [
        ('ya.ru','on'),
        ('google.com','on'),
        ('navalny.com','on'),
        ('102.com','off'),
        ('noname.shop','off'),
        ('q9lwbz65oyko.io','off'),
        ('5dq3ti-fgb6z.edu','off'),
    ]
)
def test_host(hostname, answer):
    assert is_alive_host(hostname) == answer
