# corenlp_pywrap
##CoreNLP v3.6.0
###Powerfull python wrapper for Stanford CoreNLP project
- Works only with python 3.x
- Beta version equiped with basic output fetch of stanfornlp
- 
####Install
>pip install corenlp_pywrap

####Usage
```python
from corenlp_pywrap import pywrap
cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=full_annotator_list)
\#full_annotator_list = "tokenize", "cleanxml", "ssplit", "pos", "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", "relation", "natlog", "quote"
\#Calling basic function which would return a 'requests' object
out = cn.basic(data, out_format='json')
```
Remember 'out' would be 'requests' object, you can get information by using out.text or out.json()