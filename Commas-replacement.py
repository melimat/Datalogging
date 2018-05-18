# -*- coding: utf-8 -*-
import sys
import os



def charReplacement(inputFilePath, outputFileDir, charToReplace, replacementChar):
	inputPathArray = inputFilePath.split("/")
	inputName = inputPathArray[len(inputPathArray) - 1]
	inputNameArray = inputName.split(".")
	outputName = inputNameArray[0] + "_replaced" + ".txt"
	outputPath = os.path.join(outputFileDir, outputName)
	print(("InputFilePath: " + inputFilePath))
	print(("InputFileName: " + inputName))
	print(("OutputFileName: " + outputName))
	print(("OutputFilePath: " + outputPath))
	with open(inputFilePath, "r") as inputFile:
		fileData = inputFile.read()
		fileData = fileData.replace(charToReplace, replacementChar)
		inputFile.close()
	with open(outputPath, "w") as outputFile:
		outputFile.write(fileData)
		outputFile.close()


def main():
	inputFilePath = sys.argv[1]
	outputFilePath = sys.argv[2]
	charToReplace = sys.argv[3]
	replacementChar = sys.argv[4]
	charReplacement(inputFilePath, outputFilePath, charToReplace, replacementChar)

main()
