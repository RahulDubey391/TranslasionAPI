# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:25:44 2022

@author: Rasool
"""
import base64
import os
import json
import re
from google.cloud.vision import ImageAnnotatorClient, Feature, GcsSource, InputConfig, OutputConfig, GcsDestination, AsyncAnnotateFileRequest
from google.cloud import storage
from google.cloud import pubsub_v1
from google.cloud import translate_v2 as translate

def publish_to_speech_topic(message):
    PROJECT_ID = 'business-deck'
    topic_name = 'text_to_speech'
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)
    message_json = json.dumps({
    'data': {'message': message},
    })
    message = message_json.encode('utf-8')
    publish_future = publisher.publish(topic_path, data=message)
    publish_future.result()

def pdftexttranslate(event, context):
    
    message = {}
    res = base64.b64decode(event['data'])
    json_res = json.loads(res)
    print(json_res)
    filename = json_res['data']['message']['filename']
    pages = json_res['data']['message']['pages']
    translated_pages = {}
    for page in pages.keys():
        tc = translate.Client()
        response_text = tc.translate(pages[page],target_language='hi')['translatedText']
        print(response_text)
        translated_pages[page] = response_text         
    
    message['filename'] = filename
    message['pages'] = translated_pages 
    
    publish_to_speech_topic(message)