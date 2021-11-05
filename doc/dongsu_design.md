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

* 자연어 문장을 토큰(단어) 단위로 나누고(토크나이징) 형태소(어근, 접두사/접미사, 품사) 분석
* Konlpy에서 제공하는 Komoran(Korea Morphological Analyzer) 분석기 사용
* 사용자 사전 구축(tsv 포맷 사용, Tab으로 단어/품사 구분)
  * ![사용자 사전](./img/사용자정의용어_정의.png)

### 의도 분석

* CNN(Convolutional Neural Network) 모델 사용
* Keras에서 제공하는 TensorFlow 사용
* 학습 모델 'intent_model.h5' 저장
* 정확도: 99.5%, 손실: 0.004%

![의도 분석 코드](./img/의도_분석_코드.png)
![챗봇 학습데이터](./img/챗봇_학습데이터.png)
![의도 학습](./img/chatbot_intent_학습.png)

### 개체명 인식


## ChatBot

### ChatApp

### ChatAdapter

### BotEngine

### Caller

# 시험 및 평가

## ML Pipeline

### 형태소 분석 

![형태소분석 테스트](./img/형태소분석_테스트.png)
![형태소분석 테스트 로그](./img/형태소분석_테스트_로그.png)
