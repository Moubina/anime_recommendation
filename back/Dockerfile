FROM python:3.9

WORKDIR /app/back

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["python", "web_interface_flask.py"]
