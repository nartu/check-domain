# Инструкция по запуску приложения

1. Собрать докер контейнер

```
>> docker build -t check_domain_image .
```

2. Запустить контейнер

Вариант 1
```
>> docker run -d --name check_domain -p 9000:80 check_domain_image
```
ИЛИ

Вариант 2 (если нужен любой свободный порт)
```
>> docker run -d --name check_domain -P check_domain_image
```

3. Смотреть проект по адресу
Вариант 1
http://0.0.0.0:9000
ИЛИ
Вариант 2
Посмотреть адрес командой `docker ps -l`
