from google.cloud import pubsub_v1
from ..config.config import Config
import json

class Publisher:
    def publish_to_topic(self,message):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(Config.PROJECT_ID, Config.topic_name)
        message_json = json.dumps({
                        'data': {'message': message},
                        })

        message = message_json.encode('utf-8')
        publish_future = publisher.publish(topic_path, data=message)
        publish_future.result()