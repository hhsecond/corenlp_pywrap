import requests, json

class CoreNLP:
    annotator_full_list = ["tokenize", "cleanxml", "ssplit", "pos", 
    "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", 
    "relation", "natlog", "quote", "sentiment"]
    url = 'http://127.0.0.1:9000'

    def __init__(self, url=url, annotator_list=annotator_full_list):
        if url:
            self.url = url
        assert self.url.startswith('http'), 'url string should be prefixed with http'
CoreNLP()
        

def annotation():
    url = 'http://localhost:9000/?properties={"annotators": "ner, truecase", "outputFormat": "json"}'
    data = "AFGHANISTAN:26.6 26.6 Odhiambo to Ashraf, FOUR!!"
    r = requests.post(url, data)
    server_out = r.json()
    print(len(server_out['sentences']))
    print(server_out['sentences'][0])
    return server_out