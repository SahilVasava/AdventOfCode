import matplotlib.pyplot as plt
import numpy as np

def spaceImageFormat(img, layerSize):
    layers = []
    for x in range(0, len(img), layerSize):
        layers.append(img[x:x+layerSize])
    return layers


def checkSum(layers):
    fewestZ = len(layers[0])
    fewestZLayer = None
    count = None
    for ind,layer in enumerate(layers):
        if layer.count(0) < fewestZ:
            fewestZLayer = ind
            count = layer.count(1) * layer.count(2)
            fewestZ = layer.count(0)
    print(f'Count: {count}')
    print(f'fewestZLayer: {fewestZLayer}')


def decodeImg(layers, layerSize, width):
    image = []
    for x in range(layerSize):
#        l = lambda a : a[x] 
#        print(list(map(l,layers)))
        for layer in layers:
            if layer[x] != 2:
                image.append(layer[x])
                break
    image =  np.array(image)
    img = np.reshape(image,(-1,width))
    plt.imshow(img)
    plt.show()
    print(img)

f = open('input.txt','r')
encodedImg = [ int(x) for x in list(f.read().rstrip()) ]
width, length = 25, 6
layerSize = width*length
sifLayers = spaceImageFormat(encodedImg, layerSize)
#checkSum(sifLayers)
decodeImg(sifLayers, layerSize,width)
