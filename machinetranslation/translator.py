
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url_lt = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/f685bf84-11bc-430b-a654-51054183fd14'
apikey_lt = '7-L4UIVMo_FCBc6Nxqth5-MuZXhqgp9pyB-ODbP0dl_Q'
version_lt = '2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)

language_translator = LanguageTranslatorV3(
    version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

# function that translates english to french


def english_to_french(text):
    translation_response = language_translator.translate(
        text, model_id='en-fr')

    translation = translation_response.get_result()
    translation

    French_translation = translation['translations'][0]['translation']
    French_translation

    return French_translation


# function that translates english to german
def english_to_german(text):
    translation_response = language_translator.translate(
        text, model_id='en-de')

    translation = translation_response.get_result()
    translation

    German_translation = translation['translations'][0]['translation']
    German_translation

    return German_translation
