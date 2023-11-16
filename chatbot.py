from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import pandas as pd

nltk.download('stopwords')

df = pd.read_json('data/res.json')

questions = df['question'].values
answers = df['answers'].values

# fonction de prétraitement des questions
def preprocess(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return " ".join(filtered_tokens)


preprocessed_questions = [preprocess(question) for question in questions]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

# fonction de recherche de la question la plus similaire
def trouver_question_similaire(question, questions, vectorizer):
    question_preprocess = preprocess(question)
    question_vector = vectorizer.transform([question_preprocess])
    scores = (questions * question_vector.T).toarray()
    max_score = np.max(scores)
    index_max_score = np.argmax(scores)
    return max_score, index_max_score

while True:
    question = input("Posez votre question (ou tapez 'exit' pour quitter): ")
    if question.lower() == 'exit':
        print("Merci d'avoir utilisé notre chatbot")
        break
    similar_question = trouver_question_similaire(question, X, vectorizer)
    if similar_question[0] == 0:
        print("Je n'ai pas compris votre question")
    else:
        print(answers[similar_question[1]])

