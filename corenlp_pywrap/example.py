import pywrap as p
import logging
p.root.setLevel(logging.WARNING)
cn = p.CoreNLP()
sent = '''Well, that is it then. Zimbabwe have thrashed Afghanistan for 1.0 and FOUR runs'''
r = cn.arrange(sent)
print(len(r['index']))
print(len(r['word']))
print(r['normalizedNER'])