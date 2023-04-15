FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04 as base

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get install -y emacs git wget curl python3-pip libsndfile1-dev ffmpeg

RUN git clone https://github.com/liujing04/Retrieval-based-Voice-Conversion-WebUI.git rvc
WORKDIR /rvc
RUN git checkout 8143197b3f96b5a50c2ab7507ff01c292672ef0c

RUN pip install -r requirements.txt

RUN pip install onnxruntime
RUN pip install onnxsim

WORKDIR /
ADD dummy /


ADD hubert/hubert_base.pt /rvc
ADD pretrained* /rvc/pretrained

WORKDIR /rvc

RUN ln -s /usr/bin/python3 /usr/bin/python
