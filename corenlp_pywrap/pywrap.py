import requests, json, logging, sys

root = logging.getLogger('Root')
root.setLevel(logging.DEBUG)

lhandler = logging.StreamHandler(sys.stdout)
lhandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s [%(name)s]:%(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
lhandler.setFormatter(formatter)
root.addHandler(lhandler)

class CoreNLP:
    annotator_full_list = ["tokenize", "cleanxml", "ssplit", "pos", 
    "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", 
    "relation", "natlog", "quote"]
    url = 'http://127.0.0.1:9000'

    def __init__(self, url=url, annotator_list=annotator_full_list):        
        assert url.upper().startswith('HTTP'), 'url string should be prefixed with http'
        self.url = url

        assert isinstance(annotator_list, list), "annotators can be passed only as a python list"
        if len(annotator_list) == 14:
            root.info('Using all the annotators')
        self.annotator_list = annotator_list


    def basic(self, data, out_format='json'):
        s_string = '/?properties={"annotators": "'
        anot_string = ','.join(self.annotator_list)
        f_string = '", "outputFormat": "' + out_format + '"}' 
        current_url = self.url + s_string + anot_string + f_string

        common=set(self.annotator_list).intersection(self.annotator_full_list)
        not_suprtd_elem = set(self.annotator_list) - common
        assertion_error = 'annotator not supported: ' + str(not_suprtd_elem)
        assert not not_suprtd_elem, assertion_error

        assert isinstance(data, str) and data, 'Enter valid string input'

        try:
            r = requests.post(current_url, data, headers={'Connection': 'close'})
        except requests.exceptions.ConnectionError:
            logging.error('Connection Error, check you have server running')
            raise Exception('Check your CoreNLP Server status \n'
                'if not sure, Check the pyco doc for Server instantiation')
        if 'json' in out_format:
            server_out = r.json()
        elif 'text' in out_format:
            server_out = r.text
        else:
            root.warning('out put format given is not supported, used json instead')
            server_out = r.json()
        return server_out