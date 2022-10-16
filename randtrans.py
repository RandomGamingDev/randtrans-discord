import random
import googletrans

langs = googletrans.LANGUAGES
translator = googletrans.Translator()

def RandomlyTranslate(translate, lang, times):
    global langs
    global translator

    prevLang = lang
    for i in range(times - 1):
        currentLang = random.choice(list(langs))
        translate = translator.translate(translate, src=prevLang, dest=currentLang).text
        prevLang = currentLang
    translate = translator.translate(translate, src=prevLang, dest=lang).text
    return translate 
