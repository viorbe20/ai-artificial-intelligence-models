'''
REALIZAR UN TRABAJO QUE RECOJA LA MAYORÍA DE MÉTODOS VISTOS, PUEDES PROPONER UN PROYECTO O PUEDES REALIZAR EL QUE PROPONGO A CONTINUACIÓN

ELABORACIÓN DE UN SISTEMA DE PLN ORIENTADO A UNA TAREA ESPECÍFICA
Se propone aunar todo lo aprendido en la generación de un código que tras adquirir vía ASR la conversación de un usuario con un robot de cocina, sea capaz de hacer que éste funcione, teniendo en cuenta las siguientes limitaciones.

- El robot puede cocinar mediante calor (cocer). Esta operación requiere de una temperatura en grados Celsius y de un tiempo expresado en minutos, hasta un máximo de 120'C

- El robot puede preparar alimentos agitando un instrumento, como por ejemplo batir o remover algo (batir). Esta operación requiere de una velocidad expresada en un valor de 0-10 y de un tiempo expresado en minutos, hasta un máximo de 120.

- El robot puede parar (lo cual implica velocidad de giro 0, temperatura 0ºC, tiempo 0)

- El robot ha de poder entender frases alternativas, es decir, en lugar de batir, emplear el verbo remover, o agitar, o uso de verbos generales como "pon el robot a velocidad 5"

- El robot ha de poder entender frases compuestas, que especifiquen en un solo comando temperatura, velocidad y tiempo.

El abordaje de esta labor es sencillo:

1. Un ASR convierte la voz a texto

2. El texto es procesado:

    a) Se quitan las palabras inútiles (stop words)

    b) Se unifican mayúsculas, minúsculas y signos

    c) Se tokeniza y se etiqueta

    d) Se localizan los tokens correspondientes a verbos de acción (cocer, batir)

    e) Se localizan los tokens correspondientes a valores numéricos

    f) Se va haciendo agregación sintagmática
'''

# carga de librerías
import spacy
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

# carga de modelos
nlp = spacy.load('es_core_news_sm')
nltk.download('stopwords')
nltk.download('punkt')

# carga de palabras vacías
stop_words = set(stopwords.words('spanish'))

# carga de funciones
def remove_stop_words(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return " ".join(filtered_sentence)

def remove_punctuation(text):
    return re.sub(r'[^\w\s]','',text)

def lemmatize(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def pos_tag(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def extract_verb(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.pos_ == 'VERB']

def extract_numbers(text):
    return re.findall(r'\d+', text)

def extract_temperature(text):
    return re.findall(r'\d+ºC', text)

def extract_speed(text):
    return re.findall(r'velocidad \d+', text)

def extract_time(text):
    return re.findall(r'\d+ minutos', text)

def extract_action(text):
    return re.findall(r'cocer|batir|parar', text)

def extract_all(text):
    return {
        'action': extract_action(text),
        'temperature': extract_temperature(text),
        'speed': extract_speed(text),
        'time': extract_time(text),
        'numbers': extract_numbers(text)
    }
    
def process_text(text):
    text = text.lower()
    text = remove_stop_words(text)
    text = remove_punctuation(text)
    text = lemmatize(text)
    return text

def main():
    # Solicita al usuario que ingrese el texto
    user_text = input("Introduce el texto: ")
    
    # Procesa el texto y extrae la información
    processed_text = process_text(user_text)
    result = extract_all(processed_text)
    
    # Muestra los resultados
    print(result)
    
if __name__ == "__main__":
    main()