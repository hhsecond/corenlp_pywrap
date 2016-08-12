import pywrap as p
import logging
p.root.setLevel(logging.WARNING)
cn = p.CoreNLP()
sent = '''Well, that is it then. Zimbabwe have thrashed Afghanistan. For a long while, it looked like Afghanistan held all the aces, but they have hurtled towards a heavy defeat. Coming back to the wicket, Hamza tried to nudge this back of a length delivery to fine leg. However, he got a faint edge on it. Mutumbami showed superb reflexes to dive to his left and snaffle the catch. Players from both sides shake hands as they make their way back to the pavilion. Amir Hamza c Mutumbami b Luke Jongwe 1(12)Luke Jongwe to Amir Hamza, THAT'S OUT!! Caught!!'''
r = cn.arrange(sent)
print(len(r['index']))
print(len(r['word']))