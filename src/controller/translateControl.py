import base64
import json
from ..utilities import Translator,Publisher

class Translasion:
    def __init__(self):
        self._t_obj = Translator()
        self._p_obj = Publisher()

    def triggerTranslation(self,event,context):
        
        message = {}
        res = base64.b64decode(event['data'])
        json_res = json.loads(res)
        filename = json_res['data']['message']['filename']
        
        pages = json_res['data']['message']['pages']
        
        translated_pages = {}
        for page in pages.keys():
            response_text = self._t_obj.start_translate(page)
            translated_pages[page] = response_text         

        message['filename'] = filename
        message['pages'] = translated_pages
        self._p_obj.publish_to_topic(message)
        return 'Done'