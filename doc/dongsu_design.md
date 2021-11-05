# 설계 

## 구성요소 

![구성요소](./img/chatbot_archi.png)

## 운영체제  

* Ubuntu 20.04.3 LTS

## 개발언어 

* Python 3.8.10

## Database

* MariaDB 10.4.21

## 주요 S/W Stack

> 상세 내용은 requirements.txt 참조

* aiomysql 0.0.21 (MariaDB 관련 비동기 라이브러리)
* alembic 1.6.5 (데이터 마이그레이션 도구)
* gunicorn 20.1.0 (웹 서버 게이트웨이 인터페이스)
* gensim 4.0.1 (단어 임베딩)
* Flask 2.0.0 (어플리케이션 프레임워크)
* keras 2.6.0 (딥러닝 모델 라이브러리)
* konlpy 0.5.2 (자연어 토크나이징, 형태소 분석)
* openpyxl 3.0.7 (엑셀 관련 라이브러리)
* pandas 1.3.2 (데이터 조작 및 분석 라이브러리)
* PyMySQL 0.9.3 (MariaDB 관련 라이브러리)
* pytest 6.2.4 (단위 테스트 프레임워크)
* sanic 21.3.4 (비동기 처리 어플리케이션 프레임워크)
* scikit-learn 0.24.2 (ML 라이브러리)
* SQLAlchemy 1.4.23 (ORM 라이브러리)
* tensorflow 2.6.0 (ML 프레임워크)
* aiohttp 3.8.0 (비동기 HTTP 서버/클라이언트 라이브러리)

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
  * TestRESTFulServer

# 구현 및 적용

## DB 테이블

![DB 테이블](./img/chatbot_train_data_table.png)

## 자연어 처리 과정

![자연어 처리 과정](./img/자연어_처리_과정.png)

## ML Pipeline

### 형태소 분석

### 개체명 인식

## ChatBot

### ChatApp

### ChatAdapter

### BotEngine

### Caller

# 시험 및 평가
