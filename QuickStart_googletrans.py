# -*- coding: utf-8 -*- 

## 1. googletrans ( 야매? API )
#googletrans 는 오픈소스이며 ajax api를 사용하여 구현했다고한다.
#무료지만,  하루 사용 가능 횟수 제한됨

### 기능 
#1. 소스 언어 -> 타깃 언어 로 번역하는 기능
#2. 언어 감지 기술 ( 신뢰도 함께 )
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
