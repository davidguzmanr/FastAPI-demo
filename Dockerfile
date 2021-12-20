FROM python:3.7

RUN pip install fastapi==0.70.1 uvicorn==0.16.0 spacy==3.2.1 spacytextblob==3.0.1
RUN python3 -m spacy download en_core_web_sm

RUN mkdir -p api
COPY ./api /api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]