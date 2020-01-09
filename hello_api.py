# -*- coding: utf-8 -*- 
"""
googletrans 는 오픈소스이며 ajax api를 사용하여 구현했다고한다.
무료지만,  하루 사용 가능 횟수 제한됨
"""
import googletrans
from googletrans import Translator


test_text = "안녕하세요 구글 번역기"
translator = Translator()
trans_result = translator.translate(text=test_text,
                                    src='ko',
                                    dest='en')
print(trans_result)
print(trans_result.text)
print(trans_result.pronunciation)

support_lang = googletrans.LANGUAGES
for lang in support_lang:
    print(support_lang[lang])

print(translator.detect(test_text))

translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])

from googletrans.gtoken import TokenAcquirer
acquier = TokenAcquirer()
token = acquier.do(test_text)
print(token)

"""
Google Cloud Translation (https://cloud.google.com/translate/docs/)
구글에서 공식적으로 제공하는 API
500,000 글자 미만 공짜, 100,000 자 당 $20 
https://codechacha.com/ko/python-google-translate/
"""