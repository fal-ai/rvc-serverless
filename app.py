import os
import sys
from fal_serverless import cached, isolated

REPO_PATH = "/data/repos/mangio"

@cached
def setup_repo():
    if os.path.exists(REPO_PATH):
        return
    os.system("mkdir -p /data/repos")
    os.system(f"git clone https://github.com/Mangio621/Mangio-RVC-Fork {REPO_PATH}")

@cached
def setup_models():
    if os.path.exists(f"{REPO_PATH}/pretrained_v2/D32k.pth"):
        return
    print("Getting models...")
    os.chdir(REPO_PATH)
    os.system("mkdir -p pretrained_v2 uvr5_weights")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D32k.pth -d pretrained_v2 -o D32k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth -d pretrained_v2 -o D40k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D48k.pth -d pretrained_v2 -o D48k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G32k.pth -d pretrained_v2 -o G32k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth -d pretrained_v2 -o G40k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G48k.pth -d pretrained_v2 -o G48k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D32k.pth -d pretrained_v2 -o f0D32k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth -d pretrained_v2 -o f0D40k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D48k.pth -d pretrained_v2 -o f0D48k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G32k.pth -d pretrained_v2 -o f0G32k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth -d pretrained_v2 -o f0G40k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G48k.pth -d pretrained_v2 -o f0G48k.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP2-人声vocals+非人声instrumentals.pth -d uvr5_weights -o HP2-人声vocals+非人声instrumentals.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP5-主旋律人声vocals+其他instrumentals.pth -d uvr5_weights -o HP5-主旋律人声vocals+其他instrumentals.pth")
    os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -d ./ -o hubert_base.pt")


@isolated(
    kind="conda",
    env_yml="env.yml",
    machine_type="GPU-T4",
    exposed_port=8080,
)
def app():
    setup_repo()
    setup_models()
    os.chdir(REPO_PATH)
    sys.path.append(REPO_PATH)
    os.system("python infer-web.py --pycmd python --port 8080")
