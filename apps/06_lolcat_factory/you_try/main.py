import os
import platform
import subprocess

import requests


def printHeader():
    print("-----------------------------------")
    print("         LOLCAT FACTORY")
    print("-----------------------------------")


def getOrCreateFolder():
    currentFolder = os.path.dirname(__file__)
    catPath = os.path.join(currentFolder, "cats")
    if not os.path.exists(catPath):
        os.mkdir(catPath)
    return catPath


def getCats(catFolder: os.path):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    counter = 1
    while counter <= 8:
        nameFile = "lolcat_" + str(counter)
        namePath = os.path.join(catFolder, nameFile + ".jpg")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(namePath, "wb") as fout:
                fout.write(response.raw.read())
                counter += 1
                print(f"Downloaded cat: {nameFile}")
        else:
            print("Could not download lolcat")
            return


def main():
    printHeader()
    catPath = getOrCreateFolder()
    getCats(catPath)
    if platform.system() == "Windows":
        subprocess.call(['explorer', catPath])
    else:
        print(f"We do not support {platform.system()}")


if __name__ == "__main__":
    main()
