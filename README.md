# RVC Trainer Docker

# prerequisite

- npm: to build docker
- hugging face account: download pretrained model
- docker: to run web-ui

# Usage

1. Download pretrained all models from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/pretrained) and copy them to docker_trainer/pretrained.

2. Download pretrained_v2 all models from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/pretrained_v2) and copy them to docker_trainer/pretrained_v2.

3. Download hubert_base.pt from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main). Copy it to docker_trainer/hubert.

4. Run `npm run build:docker:trainer`

5. Put training data into trainer/raw-data

6. Launch docker image `bash start_trainer.sh`

7. In docker container, run `cp -r logs_org/mute logs/`

8. In docker container, run `python infer-web.py`

9. Access the web-ui by the browser. Open tab for training.

   - http://`<address>`:7865/

10. Enter the speaker's name. Foler name includes the training data is `/rvc/raw-data`.

11. Run the training as usual.

12. The weights is in trainer/weights. `.index` is in trainer/logs/<name>/

13. Run with [VC_Client](https://github.com/w-okada/voice-changer)!

# RVC v2

Select v2 like as the below image.

![image](https://github.com/w-okada/rvc-trainer-docker/assets/48346627/71c86431-6b22-475e-969e-33e7616f3e99)
