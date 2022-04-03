from google.cloud import translate_v2 as translate

class Translator:
    def start_translate(self,page):
        tc = translate.Client()
        response_text = tc.translate(page,target_language='hi')['translatedText']
        return response_text