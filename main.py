from src import Translasion

def triggerFunction(event, context):
    tra = Translasion()
    return tra.triggerTranslation(event, context)