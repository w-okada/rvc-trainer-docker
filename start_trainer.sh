#!/bin/bash
set -eu

DOCKER_IMAGE=rvc-trainer

docker run --gpus all --rm -ti --shm-size=1024M \
    -v `pwd`/trainer/weights:/rvc/weights \
    -v `pwd`/trainer/logs:/rvc/logs \
    -v `pwd`/trainer/raw-data:/rvc/raw-data \
    -p 7865:7865 \
    $DOCKER_IMAGE /bin/bash

