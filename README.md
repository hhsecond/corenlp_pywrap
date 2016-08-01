# corenlp_pywrap
##CoreNLP v3.6.0
###Powerfull python wrapper for Stanford CoreNLP project
- Works only with python 3.x
- Beta version equiped with basic output fetch of stanfornlp
- 
####Install
>pip install corenlp_pywrap
####Usage
>from corenlp_pywrap import pywrap
>cn = pywrap.CoreNLP(url, annotator_list)
- If you want to use the default url and all annotators from stanford
>cn = pywrap.CoreNLP()
- Calling basic function which would return a 'requests' object
>out = cn.basic(data, out_format) #default out_format is json
Remember 'out' would be 'requests' object, you can get information by using out.text or out.json()