## Установка бота

Установка предусматривает ОС Ubuntu 20.04 или выше.

1. Установите докер на ОС:
   1. sudo apt-get install docker docker-compose
2. Скачайте бота:
   1. git clone https://github.com/Latand/AskQuestion
   2. Перейдите в папку AskQuestion
3. Переименуйте файл `.env.dist` в `.env`
4. Заполните переменные в файле `.env`
5. В консоли введите `docker-compose up`