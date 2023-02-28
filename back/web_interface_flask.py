import os
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return render_template('web.html')

metrics.info("app_info", "App Info, test", version="1.0.0")

@app.route('/submit', methods=['POST'])
@metrics.counter('submit_counter', 'Number of form submissions')
def submit():
    title = request.form.get('title')
    synopsis = request.form.get('synopsis')
    genre = request.form.get('genre')
    anime_type = request.form.get('anime_type')
    producer = request.form.get('producer')
    studio = request.form.get('studio')

    #Tout mettre dans un DF
    data = {
        'Title': [title],
        'Synopsis': [synopsis],
        'Genre': [genre],
        'Type': [anime_type],
        'Producer': [producer],
        'Studio': [studio]
    }
    df = pd.DataFrame(data)

    # Créer mes vecteurs et categorical
    synopsis_vector = joblib.load('/app/models/synopsis_vectorize.pkl')
    title_vector = joblib.load('/app/models/title_vectorizer.pkl')

    encoder = LabelEncoder()
    encoder.classes_ = np.load('/app/models/categorical_encoded.npy')

    title_matrix = title_vector.transform(df['Title'])
    synopsis_matrix = synopsis_vector.transform(df['Synopsis'])

    title_feature_names = title_vector.get_feature_names_out()
    synopsis_feature_names = synopsis_vector.get_feature_names_out()

    df['Genre'] = pd.factorize(df['Genre'])[0]
    df['Type'] = pd.factorize(df['Type'])[0]
    df['Studio'] = pd.factorize(df['Studio'])[0]
    df['Producer'] = pd.factorize(df['Producer'])[0]

    
    encoder = LabelEncoder()
    encoder.classes_ = np.load('/app/models/categorical_encoded.npy')

    
    genre_encoded = encoder.transform(df['Genre'])
    type_encoded = encoder.transform(df['Type'])
    studio_encoded = encoder.transform(df['Studio'])
    producer_encoded = encoder.transform(df['Producer'])


    X_vector = pd.concat([pd.DataFrame(title_matrix.toarray(), columns=title_feature_names), 
                      pd.DataFrame(synopsis_matrix.toarray(), columns=synopsis_feature_names)], axis=1)

    X_categorical = pd.concat([pd.DataFrame(df['Genre'], columns=['Genre']), 
                           pd.DataFrame(df['Type'], columns=['Type']),
                           pd.DataFrame(df['Studio'], columns=['Studio']),
                           pd.DataFrame(df['Producer'], columns=['Producer'])], axis=1)
    
    X = pd.concat([X_vector, X_categorical], axis=1)

    print(X)
    model = joblib.load('/app/models/rf_model.pkl')

    y_pred = model.predict(X)
    
    # Faites quelque chose avec les informations entrées ici
    
    print(request.form)
    
    return 'Informations soumises : {}'.format(y_pred)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='5001')