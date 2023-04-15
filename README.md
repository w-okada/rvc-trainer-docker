# RVC Trainer Docker

# prerequisite

- npm: to build docker
- hugging face account: download pretrained model
- docker: to run web-ui

# Usage

1. Download pretrained all models from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/pretrained) and copy them to docker_trainer/pretrained.

2. Download hubert_base.pt from [here](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main). Copy it to docker_trainer/hubert.

3. Run `npm run build:docker:trainer`

4. Put training data into trainer/raw-data

5. Launch docker image `bash start_trainer.sh`

6. In docker container, run `cp -r logs_org/mute logs/`

7. In docker container, run `python infer-web.py`

8. Access the web-ui by the browser. Open tab for training.

   - http://`<address>`:7865/

9. Enter the speaker's name. Foler name includes the training data is `/rvc/raw-data`.

10. Run the training as usual.

11. The weights is in trainer/weights

12. Run with [VC_Client](https://github.com/w-okada/voice-changer)!
