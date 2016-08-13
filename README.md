# corenlp_pywrap 1.0.4
######Powerfull python wrapper for Stanford CoreNLP project

[![GitHub release](https://img.shields.io/badge/release-1.0.4-green.svg?maxAge=2592000)](https://github.com/hhsecond/corenlp_pywrap/releases) [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/hhsecond/corenlp_pywrap/blob/master/LICENCE.txt) [![PyPI](https://img.shields.io/pypi/wheel/Django.svg?maxAge=2592000)](https://pypi.python.org/pypi/corenlp_pywrap)


##CoreNLP v3.6.0
- Update your version (both CoreNLP and corenlp_pywrap) for bug fixes and more features
- Works only with python 3.x


###Pywrap Doc
    
####Install
>pip install corenlp_pywrap

or

>pip3 installl corenlp_pywrap

####Usage
```python
from corenlp_pywrap import pywrap
cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=full_annotator_list)
#full_annotator_list = ["tokenize", "cleanxml", "ssplit", "pos", "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", "relation", "natlog", "quote"]

#Calling basic function which would return a 'requests' object
out = cn.basic(data, out_format='json')
```
Remember 'out' would be 'requests' object, you can get information by using out.text or out.json()

Pywrap does not inherently support 'Sentiment' now as the downloadable server version of CoreNLP doesn't have 'Sentiment' support. But there is a hack for you to use (if you are sure that your server version is the newest one and has the support)
- You can give sentiment as an attribute to annotator_list while instantiating the class object
- or
```
annotator_list = CoreNLP.full_annotator_list + ['sentiment']
```
    
####Custom Function
- arrange() can be used for getting formatted output
- Format is given below
```python
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
```
- arrange() would return token_dict which is in the above format.
- arrange() would work only for 'sentences' now. More features like 'enhanceddependancies' are coming in future releases
- Usage:
```python
from corenlp_pywrap import pywrap
cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=full_annotator_list)
#full_annotator_list = ["tokenize", "cleanxml", "ssplit", "pos", "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", "relation", "natlog", "quote"]

#custom function
token_dict = cn.arrange(data)

#example out: token_dict['index'] would give you something like this - [1,2,3,4]
```

    
####Server Instantiation Error
- If you don't have the CoreNLP server downloaded, please download the server [here](http://stanfordnlp.github.io/CoreNLP/download.html)
- Make sure you have Jave 8+ version installed
- CD to the downloaded folder
- Follow below commands
```
# Run the server using all jars in the current directory (e.g., the CoreNLP home directory)
# port and timeout are optional
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer [port] [timeout]
```
- Verify the server instance in the browser

> http://localhost:port/

replace 'port' with the port number you have given. if you didn't give any port number, port would be 9000

> http://localhost:9000/


    
####Debugging & Logging
- Pywrap using logging module for logging and debugging.
- Default logging level is set to 'warning'
- If you need more verbose logs for debugging or logging purpose make changes to the logging values

- Default log facilities
```python
root = logging.getLogger('Root')
root.setLevel(logging.WARNING)

lhandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
                '%(asctime)s [%(name)s]:%(levelname)s - %(message)s',
                '%Y-%m-%d %H:%M:%S')
lhandler.setFormatter(formatter)
root.addHandler(lhandler)
```

- You can modify each of them just like below given example
```python
import corenlp_pywrap as cp
import logging
cp.pywrap.root.setLevel(logging.DEBUG)
```
