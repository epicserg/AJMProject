import pylab
def drawPic(imageMap):
    pylab.figure(1)
    pylab.imshow(imageMap, interpolation='nearest')
    pylab.grid(True)
    pylab.show()  

filename='output.txt'
f = open(filename, "r")
text = f.read()
picture=eval(text)
drawPic(picture)
