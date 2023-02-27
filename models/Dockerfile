FROM python:3.9

WORKDIR /app/models

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 6000

COPY categorical_encoded.npy .
COPY genre_enco.pkl .
COPY producer_enco.pkl .
COPY rf_model.pkl .
COPY studio_enco.pkl .
COPY synopsis_vectorize.pkl .
COPY title_vectorizer.pkl .
COPY type_enco.pkl .

CMD ["python"]