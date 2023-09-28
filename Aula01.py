from spacy import blank

nlp = blank('pt')

doc = nlp('Eduardo foi a feira.')

print(doc[0])