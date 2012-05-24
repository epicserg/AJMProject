import AjmScanner
import pylab

def removeValuesFromList(theList, val):
        while val in theList:
            theList.remove(val)

            
def loadInfo(fileName):            
    f = open(fileName, 'r')
    allTheInfo=[]#save all info in memory
    for line in f:
        locList=line.split(" ")
        removeValuesFromList(locList,'C')
        removeValuesFromList(locList,'\n')
        removeValuesFromList(locList,'')
        #print locList
        allTheInfo.append(locList)

    allTheInfo.pop(0)
    f.close()
    return allTheInfo
def rotatePic(gridArray):
    returnMatrix=[]
    for i in range(len(gridArray[0])):
        locArray=[]
        for j in range(len(gridArray)):
           locArray.append(gridArray[j][len(gridArray[0])-i-1])
        returnMatrix.append(locArray)
    return returnMatrix

def findMeasure(time,measureArray):
    returnValue=0
    for element in measureArray:
        locData=element[2].split("/")
        if(locData[1]==time):
            returnValue= element[1]
            break
    #TODO make every returnValue smaller than 1 , so we can view it
    returnValue=float(returnValue)
    ret =(float) (returnValue)/100
    return ret       
            
    
def buildThermoMap(timeArray,measureArray):
    imageMap=[]
    
    for row in timeArray:
        imageRow=[]
        for element in row:
            
            imageRow.append(findMeasure(element,measureArray))
            
        imageMap.append(imageRow)    
    return imageMap    
  


def drawPic(imageMap):
    pylab.figure(1)
    pylab.imshow(imageMap, interpolation='nearest')
    pylab.grid(True)
    pylab.show()    



def rotatePic(gridArray):
    returnMatrix=[]
    for i in range(len(gridArray[0])):
        locArray=[]
        for j in range(len(gridArray)):
           locArray.append(gridArray[j][len(gridArray[0])-i-1])
        returnMatrix.append(locArray)
    return returnMatrix

def findMax(matrix):
    maxvalue=matrix[0][0]
    for row in matrix:
        for element in row:
            if(element>maxvalue):
                maxvalue=element
    return maxvalue            

def findMin(matrix):
    minvalue=matrix[0][0]
    for row in matrix:
        for element in row:
            if(element<minvalue):
                minvalue=element
    return minvalue

#main test
'''
scanAll :::
esimene argument :m66tmisi esimeses reas,
teine argument, kui palju ridu
kolmas arg:: ooteaeg
neljas : samma pikkus
'''
timeArray=AjmScanner.scanAll(20,7,1.2,7)
print "please put a file into a programm folder ,name it 'data.txt' and press 1"
proceed=input()
thermoData=loadInfo('data.txt')


#print timeArray
imageMap=buildThermoMap(timeArray,thermoData)
#print imageMap
drawPic(rotatePic(imageMap))
#print "maxTemp is "+str(findMax(imageMap))+" min temp was "+str(findMax(imageMap))

'''
#test for loading and finding data
thermoData=loadInfo('data.txt')
#print thermoData
print findMeasure('12:58:51',thermoData)
'''
