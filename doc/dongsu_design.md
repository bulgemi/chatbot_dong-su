# 설계 

## 구성요소 

![구성요소](./img/chatbot_archi.png)

## 운영체제  

* Ubuntu 20.04.3 LTS

## 개발언어 

* Python 3.8.10

## Database

* MariaDB 10.4.21

## S/W Stack

> 상세 내용은 requirements.txt 참조

* aiomysql 0.0.21
* alembic 1.6.5
* gunicorn 20.1.0
* gensim 4.0.1
* Flask 2.0.0
* keras 2.6.0
* konlpy 0.5.2
* openpyxl 3.0.7
* pandas 1.3.2
* PyMySQL 0.9.3
* pytest 6.2.4
* sanic 21.3.4
* scikit-learn 0.24.2
* SQLAlchemy 1.4.23
* tensorflow 2.6.0

## Source Directory

* CHATBOT_HOME
  * BotEngine
    * config
    * tests
    * app
  * WebChatbotAdapter 
    * app
      * adapter
      * static
      * templates
    * tests
  * MlPipeLine
    * train_tools
    * models
      * intent
      * ner
    * utils
    * config
    * tests
  * WordCollector
    * config
    * tests
    * app

# 구현 및 적용

# 시험 및 평가
