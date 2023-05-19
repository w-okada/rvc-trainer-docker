FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04 as base

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get install -y emacs git wget curl python3-pip libsndfile1-dev ffmpeg

RUN git clone https://github.com/liujing04/Retrieval-based-Voice-Conversion-WebUI.git rvc
WORKDIR /rvc
RUN git checkout 0fbfa1d62b43fdaeb774cfea96ad14f41296d553
RUN mv logs logs_org

RUN pip install -r requirements.txt


ADD hubert/hubert_base.pt /rvc
ADD pretrained* /rvc/pretrained
ADD pretrained_v2* /rvc/pretrained_v2


RUN ln -s /usr/bin/python3 /usr/bin/python

ADD dummy /

WORKDIR /rvc

