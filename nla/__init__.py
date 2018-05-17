import sys
from automagica.activities import *
from understanding import Understanding
import os

def main():
    understand = Understanding('wit', api_key='WNZMJCTA2HHQ24IGMBLOWSRH643WXBW2')
    filename = sys.argv[1]
    with open(os.path.join(os.getcwd(),filename)) as f:
        for line in f.readlines():
            result = understand.parse(line)
            entities = result['entities']
            intent = entities['intent'][0]
            entities.pop('intent', None)

            if intent['confidence'] > 0.90:
                if intent['value'] == 'run_application':
                    application = entities.get('application')
                    if application:
                        application = application[0]['value']
                        if application in ['chrome','the browser']:
                            browser = ChromeBrowser()
                        else:
                            exit()

                elif intent['value'] == 'browser_get':
                    url = entities.get('url')
                    if url:
                        url = url[0]['value']
                        browser.get('https://' + url)
                    else:
                        print('I need an URL!')
                        exit()

                elif intent['value'] == 'enter_search':
                    query = entities.get('query')
                    if query:
                        query = query[0]['value']
                        Type(text=query)
                        PressHotkey('enter')
                    else:
                        print('I dont understand your query')
                        exit()

                elif intent['value'] == 'click':
                    ordinal = entities.get('ordinal')
                    if ordinal:
                        ordinal = ordinal[0]['value']
                        browser.find_elements_by_tag_name('a')[ordinal].click()
                    else:
                        browser.find_elements_by_tag_name('a')[0].click()
