import pickle
import os

#введення спику
def inputFile(fileName):
    file = open(fileName, "wb")
    ampule={}                                                    #характеристики ампули

    num = int(input("Number of ampules: "))
    if num<=0:
        print("Error, no information given")
    for i in range(num):
        ampule["name"] = input("Name: ")                         #ім'я   
        ampule["hours"] = int(input("Hours: "))                  #годин дії
        ampule["minutes"] = int(input("Minutes: "))              #хвилин дії
        ampule["daysStored"] = int(input("Days stored: "))       #днів зберігання 
        ampule["daysMax"] = int(input("Days can be stored: "))   #срок придатності
        print("")

        if ampule["minutes"]>=60:
            addHours=ampule["minutes"]//60
            ampule["hours"]+=addHours
            ampule["minutes"]-=addHours*60
        if ampule["hours"]>99:
            ampule["hours"]=99

        pickle.dump(ampule, file)

    file.close()

#виведення списку
def outputFile(fileName):
    file = open(fileName, "rb")
    size=file.seek(0, 2)
    file.seek(0)

    while file.tell()<size:
        ampule=pickle.load(file)

        if ampule["daysMax"]-ampule["daysStored"]<0:
            print("AMPULE EXPIRED!")
        elif ampule["daysMax"]-ampule["daysStored"]<10:
            print("AMPULE ALMOST EXPIRED!")
        print("Name:", ampule["name"])
        print("Effective after opening for: ", ampule["hours"],"h:",ampule["minutes"],"m", sep="")
        print("Stored for: {:.1f} years\nCan be stored for: {:.1f} years".format(ampule["daysStored"]/365, ampule["daysMax"]/365))
        print("")

    file.close()

#видалення зайвих ампул
def removeDate(fileName):
    tempName="tempFile.txt"
    file = open(fileName, "rb")
    tempFile = open(tempName, "wb")
    size=file.seek(0, 2)
    file.seek(0)

    while file.tell()<size:
        ampule=pickle.load(file)
        if ampule["daysStored"]<=365:
            pickle.dump(ampule, tempFile)
    file.close()
    tempFile.close()

    os.remove(fileName)
    os.rename(tempName, fileName)
