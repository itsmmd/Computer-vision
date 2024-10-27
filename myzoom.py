#محمد ایمانیه تمرینی  که عددی از کاربر بگیرد و به همان میزان بر روی تصویر زوم کند

import cv2

def resize_image(image, scale_factor):
   
    percent_scale = scale_factor / 100.0

 
    if percent_scale > 0:
        new_size = (int(image.shape[1] * (1 + percent_scale)), int(image.shape[0] * (1 + percent_scale)))
        resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)
    elif percent_scale < 0:
        new_size = (int(image.shape[1] * (1 + percent_scale)), int(image.shape[0] * (1 + percent_scale)))
        resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)
    else:
        resized_image = image  

    center_x, center_y = resized_image.shape[1] // 2, resized_image.shape[0] // 2
    original_center_x, original_center_y = image.shape[1] // 2, image.shape[0] // 2
    
 
    crop_x1 = max(0, center_x - original_center_x)
    crop_y1 = max(0, center_y - original_center_y)
    crop_x2 = min(resized_image.shape[1], center_x + original_center_x)
    crop_y2 = min(resized_image.shape[0], center_y + original_center_y)
    
  
    cropped_image = resized_image[crop_y1:crop_y2, crop_x1:crop_x2]

   
    cv2.imshow('Resized and Centered Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"D:\Python\photo.jpg"  
image = cv2.imread(image_path)  


if image is None:
    print("Error: File not found ")
else:
    scale_factor = int(input("Please enter your number:"))  
  
    resize_image(image, scale_factor)
