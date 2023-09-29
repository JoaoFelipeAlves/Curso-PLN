from spacy import load #Carrega um modelo!

nlp = load('pt_core_news_sm')

doc = nlp(
    'Eduardo foi a feira. Comprou dois pasteis.'
)

for sent in doc.sents: #Separa 'doc' em sentenças, e printa elas
    print(sent)