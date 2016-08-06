import requests, json, logging, sys

root = logging.getLogger('Root')
root.setLevel(logging.INFO)

lhandler = logging.StreamHandler(sys.stdout)
lhandler.setLevel(logging.INFO)
formatter = logging.Formatter(
                '%(asctime)s [%(name)s]:%(levelname)s - %(message)s',
                '%Y-%m-%d %H:%M:%S')
lhandler.setFormatter(formatter)
root.addHandler(lhandler)

class CoreNLP:
    annotator_full_list = ["tokenize", "cleanxml", "ssplit", "pos", 
    "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", 
    "relation", "natlog", "quote"]
    url = 'http://127.0.0.1:9000'

    def __init__(self, url=url, annotator_list=annotator_full_list):        
        assert url.upper().startswith('HTTP'), \
            'url string should be prefixed with http'
        if 'SENTIMENT' in map(str.upper, annotator_list):
            root.warning('You are using "Sentiment" annotator which is'\
                'not supported by Old version of CoreNLP')
            
        if url.endswith('/'):
            self.url = url[:-1]
        else:
            self.url = url

        assert isinstance(annotator_list, list), \
            'annotators can be passed only as a python list'
        if len(annotator_list) == 14:
            root.info('Using all the annotators, It might take a while')

        self.annotator_list = annotator_list
        
        common=set(self.annotator_list).intersection(self.annotator_full_list)
        not_suprtd_elem = set(self.annotator_list) - common
        assertion_error = 'annotator not supported: ' + str(not_suprtd_elem)
        assert not not_suprtd_elem, assertion_error

    def server_connection(current_url, data):
        try:
            server_out = requests.post(current_url, 
                                        data, 
                                        headers={'Connection': 'close'})
        except requests.exceptions.ConnectionError:
            root.error('Connection Error, check you have server running')
            raise Exception('Check your CoreNLP Server status \n'
                'if not sure, Check the pywrap doc for Server instantiation')
        return server_out

    def basic(self, data, out_format='json', serializer=''):
        format_list = ['JSON', 'XML', 'TEXT', 'SERIALIZED']
        assert out_format.upper() in format_list, \
            'output format not supported, check stanford doc'
        
        if out_format.upper() == 'SERIALIZED' and not serializer:
            root.info(
                'Default Serializer is using - ' + 
                'edu.stanford.nlp.pipeline.ProtobufAnnotationSerializer')
            serializer = ('edu.stanford.nlp.pipeline.'
                'ProtobufAnnotationSerializer')
            
        s_string = '/?properties={"annotators": "'
        anot_string = ','.join(self.annotator_list)
        m_string = '", "outputFormat": "' + out_format
        f_string = '", "serializer": "' + serializer + '"}'
        current_url = self.url + s_string + anot_string + m_string + f_string

        assert isinstance(data, str) and data, 'Enter valid string input'
        
        root.debug('Trying: ' + current_url)
        return server_connection(current_url, data)
    
    def tokensregex(self, data, pattern, custom_filter):
        root.info('TokenRegex started')
        return self.regex('/tokensregex', data, pattern, custom_filter)

    def semgrex(self, data, pattern, custom_filter):
        root.info('SemRegex started')
        return self.regex('/semgrex', data, pattern, custom_filter)

    def regex(self, endpoint, data, pattern, custom_filter):
        url_string = '/?pattern=' + str(pattern) +'&filter=' + custom_filter 
        current_url = self.url + endpoint + url_string
        root.info('Returning the data requested')
        return server_connection(current_url, data)