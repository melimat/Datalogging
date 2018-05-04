# -*- coding: utf-8 -*-

#filePath = str(input("Here type or paste your path to the source file: "))
filePath ="/home/melimat/Downloads/Trefny.txt"


def charReplacement(path, charToReplace, replacementChar):
    with open(path, "r+") as sourceFile:
        fileData = sourceFile.read()
        fileData = fileData.replace(charToReplace, replacementChar)
        sourceFile.close()
    with open(path, "w") as sourceFile:
        sourceFile.write(fileData)
        sourceFile.close()
charReplacement(filePath, ",", ".")

