# RVC Trainer Docker

# prerequisite

- npm: to build docker
- hugging face account: download pretrained model
- docker: to run web-ui

# Usage

1. Download pretrained all models from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/pretrained) and copy them to docker_trainer/pretrained.

2. Download hubert_base.pt from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main). Copy it to docker_trainer/hubert.

3. Download mute from [here](https://github.com/liujing04/Retrieval-based-Voice-Conversion-WebUI/tree/main/logs/mute/0_gt_wavs). Copy them to trainer/logs/mute/0_gt_wavs/

4. Run `npm run build:docker:trainer`

5. Put training data into trainer/raw-data

6. Launch docker image `bash start_trainer.sh`

7. In docker container, run `python infer-web.py`

8. Access the web-ui by the browser. Open tab for training.

   - http://`<address>`:7865/

9. Enter the speaker's name. Foler name includes the training data is `/rvc/raw-data`.
10. run the training as usual.

11. the weights is in trainer/weights
