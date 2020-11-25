# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выкатить куда-либо с помощью github-actions/gitlab/jenkins/etc
