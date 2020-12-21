FROM pytorch/pytorch:latest

MAINTAINER OPilgrim
RUN cd ~
RUN apt-get update
RUN apt-get install wget -y
RUN apt-get install vim -y

RUN apt-get install git -y
RUN pip install flask
RUN pip install tensorboard==2.3.0
RUN pip install nltk==3.5
RUN git clone https://github.com/OPilgrim/Couplet.git
RUN cd Couplet && wget https://github.com/wb14123/couplet-dataset/releases/download/1.0/couplet.tar.gz && tar -zxvf couplet.tar.gz && rm -rf couplet.tar.gz 
RUN mkdir output && tar -zxvf init_output.tar.gz && mv Couplet/output/Transformer_100.bin output && rm -rf Couplet
WORKDIR ~/Couplet
