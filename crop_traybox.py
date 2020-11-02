#author: Yuita Arum Sari
import cv2
import os

def preprocessing_benchmark(img):
    image =cv2.imread(img)
    height, width, depth = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    (thresh, img_bin) = cv2.threshold(blurred, 128, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    _, contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    numrect =0
    listx =[]
    listy =[]
    listw =[]
    listh =[]
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        # cv2.drawContours(gray, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        # print ('x-y=', x, y)

        if(x!=0 and y!=0):
            if (len(approx==4)): #detected as rectangle
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image, "Object"+str(numrect+1), (x+5, y+100), font, 1, (200, 206, 106))
                numrect+=1
                x,y,w,h = cv2.boundingRect(approx)
                # print('xy', x,y,w,h)
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)
                listx.append(x)
                listy.append(y)
                listw.append(w)
                listh.append(h)

    # cv2.imshow('img',image)
    # print ('Number of Compartment=',numrect)

    return image, width, height, listx, listy, listw, listh

def cropTraybox(impath):
    file_benchmark ='cropbenchmark/_trayblankblack.jpeg'
    
    [result_im, width, height, lx, ly, lw, lh ]= preprocessing_benchmark(file_benchmark)
    # print ('width=', width, ' and height=', height)
    # for i in range(0, len(lx)):
    #     print (lx[i], ly[i], lh[i], lw[i])

    image =cv2.imread(impath)
    image = cv2.resize(image, (width, height))

    cropped = []
    for i in range(0, len(ly)): #len(ly) 0,1 object 4, 1,2 object2, 2,3 object1
        crop = image[ly[i]:ly[i]+lh[i], lx[i]:lx[i]+lw[i]]
        cropped.append(crop)
    return cropped