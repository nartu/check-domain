"""
check domain
"""
import requests

def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        headers = {'user-agent': 'test-app/0.0.1'}
        host = 'http://'+hostname
        r = requests.get(host, headers=headers, timeout=5)
    except Exception as e:
        return 'off'
        # requests.exceptions.
        # return e.__class__.__name__
    # else:
    #     print(r.status_code)

    if  100 <= r.status_code < 400:
        return 'on'
    else:
        return 'off'

# hostname = "ya.ru"
# ans = is_alive_host(hostname)
# print(ans)
