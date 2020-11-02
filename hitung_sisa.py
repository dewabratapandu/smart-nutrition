#author: Yuita Arum Sari
import cv2
import matplotlib.pyplot as plt
import os

def preprocessing_benchmark(img):
    image =cv2.imread(img);
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
        print ('x-y=', x, y)

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
    print ('Number of Compartment=',numrect)

    return image, width, height, listx, listy, listw, listh

#1. fungsi untuk menghasilkan segmentasi citra dari masing-masing kompartemen
def image_thresholding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_channel2 = 1
    blurred = cv2.GaussianBlur(gray[:,:,color_channel2], (35,35), 0)
    #morp
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35,35))
    img_dilation = cv2.dilate(blurred, kernel, iterations=3)
    img_erode = cv2.erode(img_dilation,kernel, iterations=3)
    # clean all noise after dilatation and erosion
    img_erode = cv2.medianBlur(img_erode, 15)
    ret, threshold = cv2.threshold(img_erode, 90, 255, 0) #ideal for blank compartment
    (ret2, threshold2) = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) #2
    bit_concatenate=cv2.bitwise_and(threshold,threshold2)
    return blurred, img_erode, threshold, threshold2, bit_concatenate

# 2.mendapatkan ukuran citra makanan dari hasil segmentasi
def getAreaInfo(file_data):
    file_benchmark ='cropbenchmark/_trayblankblack.jpeg'
    [result_im, width, height, lx, ly, lw, lh ]= preprocessing_benchmark(file_benchmark)

    k=0
    image =cv2.imread(file_data)
    new_image1 = cv2.resize(image, (width, height))
    # cv2.imshow('Resize_before_eaten', new_image1)
    list_area_compartment=[]
    for i in range(0, len(ly)): #len(ly) 0,1 object 4, 1,2 object2, 2,3 object1
            crop = new_image1[ly[i]:ly[i]+lh[i], lx[i]:lx[i]+lw[i]]
            [blurred, img_erode, threshold, threshold2, bit_concatenate]=image_thresholding(crop)
            # cv2.imshow('Bit Concat', bit_concatenate)
            hasil= cv2.countNonZero(bit_concatenate)
            list_area_compartment.append(hasil)
    return list_area_compartment

# 3. Menghitung sisa dari keseluruhan kompartemen pada tray box
def estimation(image_before, image_after, weight_bef):
    list_area_compt_bef = getAreaInfo(image_before)
    list_area_compt_aft = getAreaInfo(image_after)

    list_estimation=[]
    for count_compt in range(0, len(list_area_compt_bef)):
        if(list_area_compt_bef[count_compt] != 0):
            pred = weight_bef[count_compt]*list_area_compt_aft[count_compt]/list_area_compt_bef[count_compt]
            # list_estimation.append("% 12.2f" % pred)
            list_estimation.append(round(pred,2))
        else:
            list_estimation.append(0)
        # print("Estimation = ", str(pred), " gram(s)")
    return list_estimation

#4. Menghitung Error-ini masih sederhana sekali
def error_cal(weight_ori, weight_pred):
    listErr=[]
    for i in range(0, len(weight_pred)):
        err= abs(round(weight_ori[i]-weight_pred[i],2))
        listErr.append(err)
    return listErr

# if __name__=='__main__':
#     file_before = 'newdata/full.jpg'
#     file_after = 'newdata/sisa003.jpg'
#     weight_bef = [188, 10,0, 38]
#     weight_sisa3 =[91,5,0,0]
#     list_estimation = estimation(file_before, file_after, weight_bef)
#     print("SLE Estimation=", list_estimation)
#     print("SLE-Error=",error_cal(weight_sisa3,list_estimation))