import pywrap as p
cn = p.CoreNLP(annotator_list=['ner'])
r = cn.basic('This is Sherin')
print(r.text)