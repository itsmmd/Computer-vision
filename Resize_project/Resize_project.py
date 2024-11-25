#تمرین تغییر اندازه تصویر محمد ایمانیه
import cv2
import numpy as np

def process_image(image_path):

    original_image = cv2.imread(image_path)
    resized_image = cv2.resize(original_image, (900, 900))
    height, width, _ = resized_image.shape

    new_images = [np.zeros((100, 100, 3), dtype=np.uint8) for _ in range(9)]

    stride = 9
    for j in range(0, height, stride): 
        for i in range(0, width, stride):  
            for m in range(9):
                if i + m < width:
                    pixel = resized_image[j, i + m]
                    new_images[m][j // stride, i // stride] = pixel

    for img in new_images:
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

process_image('1.jpg')
