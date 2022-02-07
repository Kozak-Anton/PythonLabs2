#введення текстового файлу
def inputFile(fileName): 
    file=open(fileName, "wt");
    while True:
        line=input()
        if not line:
            break
        file.write(line+"\n")
    file.close()

#виведення текстового файлу
def outputFile(fileName):
    file=open(fileName, "rt")
    text=file.read()
    print(text)
    file.close()

#редагування текстового файлу
def rewriteFile(initFile, editFile):
    iFile = open(initFile, "rt")
    oFile = open(editFile, "wt");

    count=0
    for line in iFile:
        count+=1
        oFile.write(str(count)+". "+line[:len(line)-1]+" "+str(len(line)-1)+"\n")
    iFile.close()
    oFile.close()

