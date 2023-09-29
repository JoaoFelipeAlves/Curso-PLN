from spacy import load #Carrega um modelo!

nlp = load('pt_core_news_sm')

doc = nlp(
    'Eduardo foi a feira. Comprou dois pasteis.'
)

print(list(doc)) #Printa a lista de tokens de "doc"

print([str(x) for x in list(doc)]) #Printa entre aspas a lista de tokens de "doc"