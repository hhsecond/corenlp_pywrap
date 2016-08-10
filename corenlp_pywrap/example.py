import pywrap as p
cn = p.CoreNLP(annotator_list=['ssplit'])
r = cn.arrange('This is Sherin')
r = r.json()
r1 = r['sentences']
#r = cn.tokensregex('The quick brown fox jumped over the lazy dog.', '(?$foxtype [{pos:JJ}]+ ) fox')
#print(r.text)