from google.cloud import translate

import os
credential_path = os.path.join(os.getcwd(), "google_credential.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
print(credential_path)


def sample_translate_text(text, target_language, project_id):
    """
    Translating Text

    Args:
      text The content to translate in string format
      target_language Required. The BCP-47 language code to use for translation.
    """

    client = translate.TranslationServiceClient()

    # TODO(developer): Uncomment and set the following variables
    # text = 'Text you wish to translate'
    # target_language = 'fr'
    # project_id = '[Google Cloud Project ID]'
    contents = [text]
    parent = client.location_path(project_id, "global")

    response = client.translate_text(
        parent=parent,
        contents=contents,
        mime_type='text/plain',  # mime types: text/plain, text/html
        source_language_code='en-US',
        target_language_code=target_language)
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))

sample_translate_text(text="FUCK", target_language='ko', project_id="api-project-696940428383")