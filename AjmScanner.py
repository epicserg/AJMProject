import serial
import time

ser=serial.Serial('COM5',9600,timeout=1)
#globalTimeArray=[][]


#either the direction is 1 or (-1)
def moveAndSave(direction,pauseLenght,scanLen):
    #next line should move camera horizontally
    ser.write('HX{0}SY{1}S'.format(0,scanLen*direction))
	ser.write('XW')
    time.sleep(pauseLenght)
    currentTime=time.ctime()
    timeElements=currentTime.split(" ")
    return timeElements[3]
    #return time.strftime('%X %x %Z')


def moveOneRow(direction,measureNumb,pauseLenght,scanLen):
    locTimeArray=[]
    for i in range(measureNumb):
        locTimeArray.append(moveAndSave(direction,pauseLenght,scanLen))
    return locTimeArray                
        
def scanAll(timesHorizont,timesVertical,pauseLenght,scanLen):
    timeArray=[]

    for i in range(timesVertical):
        print "scanning "+str(i)+" th row"
        timeArray.append(moveOneRow(1,timesHorizont,pauseLenght,scanLen))
        #next line should move camera up
        ser.write('HX{0}SY{1}S'.format(scanLen,0))
		ser.write('YW')
        time.sleep(2)
        backArray=moveOneRow(-1,timesHorizont,pauseLenght,scanLen)
        backArray.reverse()
        timeArray.append(backArray)
        
    print "first layer lenght is "+str(len(timeArray))    
    return timeArray


'''
a=scanAll(5,5,0.5)
print a               
'''
