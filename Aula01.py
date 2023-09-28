from spacy import blank

nlp = blank('pt')

doc = nlp('Eduardo foi a feira.')

token = doc[1]

print(type(token))

span = doc[0:3]

print(type(span))