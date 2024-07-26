import os

def fileList(target):
    if target is not "":
        target = f"/{target}"

    return os.popen(f'adb shell ls -a "/storage/self{target}"').read().splitlines()
