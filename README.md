# Чат-боты на Python «Распознаём речь»

Учебный проект курса "От джуна до мидла" компании Devman.

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


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).