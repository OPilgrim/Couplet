FROM pytorch/pytorch:latest

RUN apt-get update
RUN apt-get install git -y
RUN git clone https://github.com/OPilgrim/Couplet.git
RUN pip install flask
RUN pip install tensorboard==2.3.0
RUN pip install nltk==3.5
RUN pip install tqdm 
RUN apt-get install wget
RUN cd Couplet && wget https://github.com/wb14123/couplet-dataset/releases/download/1.0/couplet.tar.gz && tar -zxvf couplet.tar.gz && rm -rf couplet.tar.gz 
WORKDIR /workspace/Couplet
