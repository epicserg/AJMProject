import serial
import time

ser=serial.Serial('COM5',9600,timeout=1)
#globalTimeArray=[][]


#either the direction is 1 or (-1)
def moveAndSave(direction,pauseLenght,scanLen):
    #next line should move camera horizontally
    ser.write('HX{0}SHY{1}S'.format(0,scanLen*direction))
	#ser.write('XW')
    time.sleep(pauseLenght)
    currentTime=time.ctime()
    timeElements=currentTime.split(" ")
    return timeElements[3]
   
def fixAll():
    ser.write('!')
    time.sleep(1)
    print "calling fix all command"
    ser.write('W')
    ser.write('YW')
    ser.write('XW')

def moveOneRow(direction,measureNumb,pauseLenght,scanLen):
    #fixAll()
    locTimeArray=[]
    for i in range(measureNumb):
        locTimeArray.append(moveAndSave(direction,pauseLenght,scanLen))
    return locTimeArray                
        
def scanAll(timesHorizont,timesVertical,pauseLenght,scanLen):
    timeArray=[]
    #ser.write('!')
    time.sleep(2)
    fixAll()
    #ser.write('HX{1}SY{1}S'.format((-1.0)*timesHorizont*scanLen/2,(-1.0)*timesVertical*scanLen))
    time.sleep(2)
    for i in range(timesVertical):
        print "scanning "+str(i)+" th row"
        locLen=scanLen
        timeArray.append(moveOneRow(1,timesHorizont,pauseLenght,locLen))
        #next line should move camera up
	#print "moving up "+str(1)
        ser.write('HX{0}SY{1}S'.format((1)*scanLen-1,0))
	#fixAll()
        time.sleep(2)
        backArray=moveOneRow(-1,timesHorizont,pauseLenght,scanLen)
        print "moving up "+str(1)
        ser.write('HX{0}SY{1}S'.format((1)*scanLen-1,0))
        #fixAll()
        time.sleep(2)
        backArray.reverse()
        timeArray.append(backArray)
        
    print "first layer lenght is "+str(len(timeArray))
    ser.write('!')
    return timeArray


'''
a=scanAll(5,5,0.5)
print a               
'''
