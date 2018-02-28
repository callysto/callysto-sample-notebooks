FROM continuumio/anaconda3

RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN mkdir /opt/callysto

