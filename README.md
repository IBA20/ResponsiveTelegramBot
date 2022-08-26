# Чат-боты на Python «Распознаём речь»

Учебный проект курса "От джуна до мидла" компании Devman.
[Пример работающего бота](https://t.me/suppservbot)  
![image](https://dvmn.org/media/filer_public/7a/08/7a087983-bddd-40a3-b927-a43fb0d2f906/demo_tg_bot.gif)

## Задание

Написать бота-помощника для Telegram и VK, который отвечает на типовые вопросы с помощью нейросети. 

## Установка и запуск

1. Клонируйтие данный репозиторий.
2. Войдите на сайт [Dialogflow](https://dialogflow.cloud.google.com/) (потребуется учетная запись Google). Создайте нового агента, указав язык по умолчанию - русский. Запишите GOOGLE PROJECT ID.

3. Создайте следующие переменные окружения:

GOOGLE_APPLICATION_CREDENTIALS - путь к json-файлу с Google credentials, [инструкция](https://cloud.google.com/docs/authentication/provide-credentials-adc)  
GOOGLE_CLOUD_PROJECT - ID проекта из п.2  
TG_BOT_TOKEN - API ключ вашего телерам-бота. Создать бота и получить API ключ можно с помощью @BotFather.  
VK_TOKEN - API-ключ группы VK, [инструкция](https://pechenek.net/social-networks/vk/api-vk-poluchaem-klyuch-dostupa-token-gruppy/)
TG_CHATID - chat_id телеграм-аккаунта, куда будут отправляться логи. Чтобы получить свой chat_id, напишите в Telegram специальному боту: @userinfobot.
  
4. Загрузите в нейросеть тренировочные фразы:
```
python train.py

```  
5. Телеграм-бот запускается командой
```
python tg.py

```  
6. VK-бот запускается командой
```
python vk.py

```  
## Особенности деплоя на Heroku
Перед деплоем необходимо сделать следующее:  
1. Переменная окружения GOOGLE_APPLICATION_CREDENTIALS должна содержать строку 'google-credentials.json'    
2. В дополнительную переменную окружения GOOGLE_CREDENTIALS скопируйте содержимое вашего json-файла с Google credentials.  
3. Остальные переменные окружения создайте как описано выше в разделе Установка и запуск.
4. На вкладке Settings нажмите Add Buildpack и добавьте
```
https://github.com/gerynugrh/heroku-google-application-credentials-buildpack

```  
5. Там же добавьте стандартный пакет heroku/python


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).