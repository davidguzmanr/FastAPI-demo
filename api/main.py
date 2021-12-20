"""
A simple API to perform sentiment analysis.
"""

from fastapi import FastAPI

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

app = FastAPI()

@app.post('/sentiments')
def extract_sentiment(text: str):
    """
    Returns a dictionary with the polarity (a float within the range [-1.0, 1.0],
    where -1.0 is very negative sentiment and 1.0 very positive sentiment) and the
    subjectivity (a float within the range [0.0, 1.0], where 0.0 is very objective 
    and 1.0 is very subjective) of a text.

    Parameters
    ----------
    text: str. 
    """
    doc = nlp(text)
    response = {
        'polarity': doc._.polarity, 
        'subjectivity': doc._.subjectivity
    }

    return response