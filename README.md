## google_translate_api 테스트 ( QuickStart 코드 )
### 1. google_trans 
### 2. google-cloud-translate-api v2 ( pbmt, nmt )
### 3. google-cloud-translate-api v3 beta ( automl )

## src/main.py 를 실행하세요!
### 그전에 GCP에 로그인해서 api 사용 프로젝트에 google-cloud-translator 사용 등록해야함
### 1. dataset/input 폴더 내 *.csv 파일 로딩 (sample_input.csv)
- Index, Input 을 컬럼으로 가지는 csv 파일
### 2. google_api_v2 적용 번역
### 3. dataset/output 폴더 내 번역 결과 생성
- (sample_output.csv, input을 output으로 자동변경)
- index, input, output 를 컬럼으로 가지는 csv 파일 생성

## 진행 이슈
### API Request에 제한이 있네요. 멀티프로세싱 기능 불가능 현재로선
### sleep ( 0.5 )을 넣어야할 지경
|콘텐츠 할당량|기본|최대|기간|적용대상|
|-|-|-|-|-|
|일일 일반 모델 문자|	10억 자|	무제한|	1일|	프로젝트|
|프로젝트당 100초당 일반 모델 문자|	1,000,000자|	10,000,000자|	100초|	프로젝트|
|사용자당 프로젝트당 100초당 일반 모델 문자|	100,000자|	10,000,000자|	100초|	프로젝트와 사용자|