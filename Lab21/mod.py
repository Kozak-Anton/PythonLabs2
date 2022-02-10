#введення текстового файлу
def inputFile(fileName): 
    file=open(fileName, "wt");
    while True:
        line=input()
        if line.find(chr(26))!=-1:
            line=line[:line.find(chr(26))]
            file.write(line+"\n")
            print("")
            break
        elif not line:
            break
        file.write(line+"\n")
    file.close()

#виведення текстового файлу
def outputFile(fileName):
    file=open(fileName, "rt")
    print(file.read())
    file.close()

#редагування текстового файлу
def rewriteFile(initFile, editFile):
    iFile = open(initFile, "rt")
    oFile = open(editFile, "wt");

    count=0
    for line in iFile:
        count+=1
        oFile.write(str(count)+". "+line[:len(line)-1]+" len="+str(len(line)-1)+"\n")
    iFile.close()
    oFile.close()

