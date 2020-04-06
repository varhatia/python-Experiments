from cv2 import cv2
import glob

i = 0
images = glob.glob("./images/*.jpg")

for image in images:
    print (image)
    i = i+1
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    #cv2.imshow("Hey",re)
    #cv2.waitKey(500)
    #cv2.destroyAllWindows()
    cv2.imwrite("./images/resize_"+str(i)+".jpg",re)