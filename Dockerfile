FROM continuumio/anaconda3

RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN mkdir /opt/callysto

RUN apt-get install build-essential libdb-dev -y && \
    pip install gutenberg rdflib nltk && \
    python -m nltk.downloader popular brown

RUN pip install textblob ipyleaflet mobilechelonian metakernel plotly