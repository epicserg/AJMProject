from pylab import *
import thread
#our scanning data here
file= open('output.txt', 'r')
text=file.readline()
a=eval(text)
 
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

def rotatePic(gridArray):
    returnMatrix=[]
    for i in range(len(gridArray[0])):
        locArray=[]
        for j in range(len(gridArray)):
           locArray.append(gridArray[j][len(gridArray[0])-i-1])
        returnMatrix.append(locArray)
    return returnMatrix




def generateScale(matrix):
    b=[]
    delta=1.0*(findMax(matrix)-findMin(matrix))/100
    for i in range(100):
        c=i*delta+findMin(matrix)
        b.append(c)

    B=[]
    for j in range(10):
        B.append(b)

    return B

def showPic(matrix):
    imshow(matrix, interpolation='bilinear')
    grid(False)
    show()



print "minimum value is "+str(findMin(a)*100)
print "maxvalue is "+str(findMax(a)*100)
B=generateScale(a)
showPic(a)
showPic(B)


