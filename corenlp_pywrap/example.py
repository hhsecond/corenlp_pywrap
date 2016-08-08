import pywrap as p
cn = p.CoreNLP(annotator_list=['lemma'])
r = cn.basic('This is Sherin, I love coding\n my hobby ;')
print(r.text)