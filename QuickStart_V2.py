# setup 
# pip install google-cloud-translate
# get api-project-key from gcp console
# 
import os
credential_path = os.path.join(os.getcwd(), "google_credential.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
print(credential_path)


# Basic ( V2 )
from google.cloud import translate_v2 as translate
translate_client = translate.Client()

texts = ["안녕하세요 세계", "안녕히가세요 세계", "내가 니가 누군지 알아야 되니?"]
target = "en"
model = ['pbmt', 'nmt']
# base - pbmt ( PBMT·Phrase-based translation )
# nmt - neural machine translator
for text in texts:
    src_lang = translate_client.detect_language(text)
    print('Text: {}'.format(src_lang))
    print('Confidence: {}'.format(src_lang['confidence']))
    print('Language: {}'.format(src_lang['language']))

    result = translate_client.translate(text, 
                                        target_language=target,
                                        model='base')

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

list_available_lang = translate_client.get_languages()
for lang in list_available_lang:
    print(u'{name} ({language})'.format(**lang))


