import requests
url = 'http://localhost:9000/?properties={"annotators": "tokenize, cleanxml, ssplit, pos, lemma, ner, regexner, truecase, parse, depparse, dcoref, relation, natlog, quote", "outputFormat": "text"}'
data = '''AFGHANISTAN:26.6 26.6 Odhiambo to Ashraf, FOUR!! , short again outside off, Ashraf moves back and pulls it effortlessly to deep mid wicket fence, a convincing win in the end for the Afghans as they win the match with 23 overs to spare'''
r = requests.post(url, data)
mydict = r.text
print(mydict)