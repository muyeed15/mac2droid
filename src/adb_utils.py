import os

def fileList(target):
    if target is not "":
        target = f"/{target}"

    return os.popen(f'adb shell ls -a "/storage/self{target}"').read().splitlines()

def connectDevice(ip, code):
    return os.popen(f'adb "{ip}" "{code}"')

def activeDevice():
    return os.popen('adb device')