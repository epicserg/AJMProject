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
   
#main test
'''
scanAll :::
esimene argument :m66tmisi esimeses reas,
teine argument, kui palju ridu
kolmas arg:: ooteaeg
neljas : samma pikkus
'''
timeArray=AjmScanner.scanAll(10,5,2,10)
print "please put a file into a programm folder ,name it 'data.txt' and press 1"
proceed=input()
thermoData=loadInfo('data.txt')


print timeArray
imageMap=buildThermoMap(timeArray,thermoData)
#print imageMap
drawPic(imageMap)

'''
#test for loading and finding data
thermoData=loadInfo('data.txt')
#print thermoData
print findMeasure('12:58:51',thermoData)
'''
