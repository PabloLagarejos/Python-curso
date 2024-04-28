#instalar scikit-learn
#upgrade numpy
#upgrade scipy
#instalar wordcloud

import pandas as pd
import re
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk import SnowballStemmer
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from wordcloud import WordCloud
import seaborn as sb
from nltk.corpus import stopwords
#descarga paquetes de nltk
nltk.download('stopwords')
tweets_file='phrase.txt'
df = pd.read_csv(tweets_file,sep="::::",names=['tweet','sentimiento'])
df= df[df['sentimiento'].isin(['Positive','Neutral','Negative'])]
tweets = [tuple(x) for x in df.values]
print('Numero de tweets Cargados:{num}'.format(num=len(tweets)))
df.head(5)
#normalización de tweets
def normalize(text):
    text = re.sub(r'@[a-zA-Z0-9_]+', '', text)
    text=re.sub(r'#','',text)
    text=re.sub(r'RT','',text)
    text=re.sub(r'https?:\/\/\S+','',text)
    text=text.lower()
    text=re.sub(r'\W+','',text)
    text=re.sub(r'\s+','',text)
    return text.strip()

tweets=[(normalize(tweet),sentimiento)for tweet,sentimiento in tweets]
#CREACIÓN DE LA BOLSA DE PALABRAS:
stemmer=SnowballStemmer('spanish')
stop_words = set(stopwords.words('spanish'))
def create_bag_of_words(tweets):
    bow=[]
    for text,_ in tweets:
        words=re.findall(r'\w+',text)
        words=[stemmer.stem(word) for word in words if word not in stop_words]
        bow.append(''.join(words))
    return bow
tweets=create_bag_of_words(tweets)

#División de datos en conjunto de entrenamiento y prueba:
X_train,X_test,y_train,y_test=train_test_split(tweets,df['sentimiento'],test_size=0.2,random_state=42)
#vectorización de los datos de texto:
vectorizer = CountVectorizer()
X_train=vectorizer.fit_transform(X_train)
X_test=vectorizer.transform(X_test)

#Entrenamiento y evaluación de modelo de clasificación

classifier = MultinomialNB()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)

#Generación de gráfico de barras
sentimiento_counts=df['sentimiento'].value_counts()
plt.bar(sentimiento_counts.index,sentimiento_counts.values)
plt.xlabel('sentimiento')
plt.ylabel('Cantidad de tweets')
plt.title('Distribución de sentimientos en tweets')
plt.show()
#Generación de nubes de palabras:
all_words = ' '.join(tweets)
wordcloud = WordCloud(width=800,height=400).generate(all_words)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de Palabras Frecuentes')
plt.show()
#Segunda Generación de Nube
x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
wc = WordCloud(background_color = "white", repeat = True, mask = mask)
wc.generate(all_words)
plt.axis("off")
plt.imshow(wc, interpolation = "bilinear")
plt.show()
#Tercera Generación de Nube
texto = " David Galan Marga Hernandez Shahrzard Motamed Pablo Lagarejos Pablo Duran Jaime Sanz"
x , y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
wc = WordCloud(height = 500, width = 500, background_color = "white",
               repeat = True, mask = mask,
               contour_width = 3, contour_color = "black")
wc.generate(texto)
plt.axis("off")
plt.imshow(wc, interpolation = "bilinear")
plt.show()