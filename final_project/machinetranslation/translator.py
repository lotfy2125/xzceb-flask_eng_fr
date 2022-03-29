import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')
authenticator = IAMAuthenticator(apikey)

# create an instance of watson translator language .
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """ translate english to french  """
    frenchText = language_translator.translate(
        englishText,
        model_id='en-fr').get_result()
    print(frenchText)
    return frenchText['translations'][0]['translation']

def frenchToEnglish(frenchText):
    """ translate french to english  """
    englishText = language_translator.translate(
        frenchText,
        model_id='fr-en').get_result()
    print(englishText)
    return englishText['translations'][0]['translation']               

d1 = englishToFrench('welcome')
print(d1)
d2 = frenchToEnglish('Bonjour')
print(d2)