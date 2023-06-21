import os
from threading import Thread
from time import time

import requests


def download_file(file, folder="dist", base_path="https://res.classeasy.cn/prod/tenant/8093D9C8/"):
    header = {}

    link = f"{base_path}{file}"

    # prepare
    local_file = f"{file}"

    try:
        if not os.path.exists(f"下载/{folder}/"):
            os.mkdir(f"下载/{folder}/")
    finally:
        pass

    local_file = os.path.join(f"下载/{folder}/", f"{local_file}")

    if os.path.exists(local_file):
        print(f"本地已经存在该文件，跳过下载")

    else:
        print(f"正在下载文件，{file}")
        try:
            f = requests.get(link, headers=header)
            with open(local_file, 'wb') as code:
                code.write(f.content)
                code.flush()
        except:
            with open(os.path.join(f"logs", f"{folder}.log"), mode="a+") as logs:
                logs.write(f"{local_file} 下载失败\n")
        else:
            with open(os.path.join(f"logs", f"{folder}.log"), mode="a+") as logs:
                logs.write(f"{local_file} 下载成功\n")



class Downloader(Thread):
    def __init__(self, file, base_path, folder):
        super().__init__()
        if not base_path.startswith('https'):
            base_path = f"https://{base_path}"
        self._file = file
        self._base_path = base_path
        self._folder = folder

    def run(self) -> None:
        download_file(self._file, self._folder, self._base_path)


def download_task(obj):
    start = time()
    threads = []
    for image in obj["images"]:
        t = Downloader(file=image, folder=obj["folder"], base_path=obj["base_path"])
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("文件数量 %d" % len(threads))

    local_file = os.path.join(f"下载/{obj['folder']}/", f"0_note.md")
    with open(local_file, 'w') as code:
        code.write(obj["desc"])
        code.flush()

    end = time()
    print("下载完成 耗时：%.2f秒" % (end - start))
    return {
        "count": len(threads),
        "duration": int(end - start)
    }
