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

* sanic 21.3.4

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
