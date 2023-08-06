
from dataclasses import dataclass
import os
from time import sleep
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


@dataclass
class DownloadParams:
    url: str
    saveTo: str
    position: int


class Downloader:
    def __init__(self):
        self.params: list[DownloadParams] = []

    def pushItem(self, url: str, saveTo: str):
        self.params.append(DownloadParams(url, saveTo, len(self.params)))

    def download(self):
        with ThreadPoolExecutor() as pool:
            pool.map(self._downloadItem, self.params)
        sleep(1)

    def _downloadItem(self, params: DownloadParams):
        url = params.url
        saveTo = params.saveTo
        position = params.position
        dirname = os.path.dirname(saveTo)
        if dirname != "":
            os.makedirs(dirname, exist_ok=True)

        try:
            req = requests.get(url, stream=True, allow_redirects=True)
            content_length = req.headers.get("content-length")
            progress_bar = tqdm(
                total=int(content_length) if content_length is not None else None,  # NOQA
                leave=False,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                position=position,
            )

            # with tqdm
            with open(saveTo, "wb") as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        progress_bar.update(len(chunk))
                        f.write(chunk)

        except Exception as e:
            print(e)
        print("aadfasf2")


if __name__ == "__main__":
    downloader = Downloader()
    # Pretrained for v1
    urlDir = "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/"
    saveToDir = "docker_trainer/pretrained/"
    for f in ["D32k.pth", "D40k.pth", "D48k.pth",
              "G32k.pth", "G40k.pth", "G48k.pth",
              "f0D32k.pth", "f0D40k.pth", "f0D48k.pth",
              "f0G32k.pth", "f0G40k.pth", "f0G48k.pth"]:
        downloader.pushItem(os.path.join(urlDir, f), os.path.join(saveToDir, f))  # NOQA

    # Pretrained for v2
    urlDir = "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/"
    saveToDir = "docker_trainer/pretrained_v2/"
    for f in ["D32k.pth", "D40k.pth", "D48k.pth",
              "G32k.pth", "G40k.pth", "G48k.pth",
              "f0D32k.pth", "f0D40k.pth", "f0D48k.pth",
              "f0G32k.pth", "f0G40k.pth", "f0G48k.pth"]:
        downloader.pushItem(os.path.join(urlDir, f), os.path.join(saveToDir, f))  # NOQA

    # HUBERT
    downloader.pushItem("https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt", "docker_trainer/hubert/hubert_base.pt")  # NOQA

    downloader.download()
