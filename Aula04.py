from spacy import load #Carrega um modelo!

nlp = load('pt_core_news_sm')

doc = nlp(
    'Eduardo foi a feira.'
)

for t in doc: #para cada token em 'doc'
    print(t.text, t.shape_, t.shape) 

    #'text' extrai o texto de cada token
    #'shape_' extrai o Formato como ta escrito
    #'shape' extrai o código do token 