# corenlp_pywrap
##CoreNLP v3.6.0
###Powerfull python wrapper for Stanford CoreNLP project
- Works only with python 3.x
- Production Ready version equiped with basic output fetch of stanfornlp and custom arrange function
- 
####Install
>pip install corenlp_pywrap

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