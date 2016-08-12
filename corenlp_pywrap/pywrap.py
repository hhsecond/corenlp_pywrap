import requests, logging, sys

root = logging.getLogger('Root')
root.setLevel(logging.INFO)

lhandler = logging.StreamHandler(sys.stdout)
lhandler.setLevel(logging.WARNING)
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
    out_format = 'json'

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


    @staticmethod
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
    
   
    def url_calc(self, serializer=''):
        s_string = '/?properties={"annotators": "'
        anot_string = ','.join(self.annotator_list)
        m_string = '", "outputFormat": "' + self.out_format
        f_string = '", "serializer": "' + serializer + '"}'
        return self.url + s_string + anot_string + m_string + f_string


    def basic(self, data, out_format='json', serializer=''):
        self.out_format = out_format
        format_list = ['JSON', 'XML', 'TEXT', 'SERIALIZED']
        assert out_format.upper() in format_list, \
            'output format not supported, check stanford doc'
        
        if out_format.upper() == 'SERIALIZED' and not serializer:
            root.info(
                'Default Serializer is using - ' + 
                'edu.stanford.nlp.pipeline.ProtobufAnnotationSerializer')
            serializer = ('edu.stanford.nlp.pipeline.'
                'ProtobufAnnotationSerializer')
                
        current_url = self.url_calc(serializer)
        assert isinstance(data, str) and data, 'Enter valid string input'
        
        root.debug('Trying: ' + current_url)
        return self.server_connection(current_url, data)

    @staticmethod
    def tokensregex(data, pattern='', custom_filter=''):
        root.info('TokenRegex started')
        return CoreNLP.regex('/tokensregex', data, pattern, custom_filter)

    @staticmethod
    def semgrex(data, pattern='', custom_filter=''):
        root.info('SemRegex started')
        return CoreNLP.regex('/semgrex', data, pattern, custom_filter)

    @classmethod
    def regex(cls, endpoint, data, pattern, custom_filter):
        url_string = '/?pattern=' + str(pattern) +'&filter=' + custom_filter 
        current_url = cls.url + endpoint + url_string
        root.info('Returning the data requested')
        return cls.server_connection(current_url, data)

    @staticmethod
    def process_sentences(sentences):
        assert isinstance(sentences, list), 'it should be a list'
        index = 0
        new_index = 0
        token_dict = {
        'index':[],
        'truecaseText':[],
        'ner':[],
        'before':[],
        'originalText':[],
        'characterOffsetBegin':[],
        'lemma':[],
        'truecase':[],
        'pos':[],
        'characterOffsetEnd':[],
        'speaker':[],
        'word':[],
        'after':[]
        }
        for sentence in sentences:
            index = new_index
            tokens = sentence['tokens']
            for val in tokens:
                for key, val in val.items():
                    if key == 'index':
                        new_index = index + int(val)
                        token_dict[key].append(str(new_index))
                    else:
                        token_dict[key].append(val)
        return token_dict


    def arrange(self, data):
        root.info('Executing custom function')
        assert isinstance(data, str) and data, 'Enter valid string input'
        if 'lemma' not in self.annotator_list:
            self.annotator_list.append('lemma')
        
        current_url = self.url_calc()
        r = self.server_connection(current_url, data)
        r = r.json()
        root.debug('return json object doesnt have two values')
        rs = r['sentences']
        return self.process_sentences(rs)