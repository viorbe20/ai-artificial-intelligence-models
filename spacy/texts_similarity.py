import spacy
from spacy import displacy
from collections import Counter
import es_core_news_lg

nlp = es_core_news_lg.load()
doc1 = nlp('Carlos se come una manzana')
doc2 = nlp('María se come una ensalada')
doc3 = nlp('María y Carlos se comen un plato de pasta')
doc4 = nlp('María y Carlos ve una pelicula')

print(doc1, "<->", doc2, doc1.similarity(doc2))
print(doc1, "<->", doc3, doc1.similarity(doc3))
print(doc1, "<->", doc4, doc1.similarity(doc4))
print(doc3, "<->", doc4, doc3.similarity(doc4))


doc5 = nlp('El profesor enseña gramática')
doc6 = nlp('El docente imparte matemáticas')

print(doc5, "<->", doc6, doc5.similarity(doc6))

doc7 = nlp('Me siento cómodo sacando dinero en el banco')
doc8 = nlp('Este banco es muy cómodo')

print(doc7, "<->", doc8, doc7.similarity(doc8))