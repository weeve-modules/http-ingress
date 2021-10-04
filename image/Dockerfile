FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r image/requirements.txt
ENTRYPOINT ["python", "image/main.py"]
EXPOSE 80
