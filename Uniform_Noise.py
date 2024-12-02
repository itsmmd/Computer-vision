#mohammah imanieh uniform noise
import cv2 as cv
import numpy as np
import random as rn
import math

# مسیر تصویر
img_path = "imanieh.jpg"
img = cv.imread(img_path)
img2 = img.copy()
img3 = img.copy()
width = img.shape[1]
height = img.shape[0]

# درصد نویز
noise_percentage = float(input("Enter a percent of noise to apply: "))

def apply_uniform_noise(img2, width, height, noise_percentage):
    num_noise_pixels = int(width * height * noise_percentage / 100)
    
    for _ in range(num_noise_pixels):
        y = rn.randint(0, height - 1)
        x = rn.randint(0, width - 1)
        noise_value = rn.randint(0, 255)
        img2[y][x] = [noise_value, noise_value, noise_value]

    return img2

noise_image = apply_uniform_noise(img2, width, height, noise_percentage)

def check_extreme_pixel(pixel):
    return (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0) or (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255)

def get_neighbours(data, y, x, channel):
    neighbours = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            if 0 <= y + dy < data.shape[0] and 0 <= x + dx < data.shape[1]:
                neighbours.append(data[y + dy, x + dx, channel])
    return neighbours

def find_true_pixels(vector):
    return [val for val in vector if val != 0 and val != 255]

for y in range(1, height - 1):
    for x in range(1, width - 1):
        vector = noise_image[y, x]

        if check_extreme_pixel(vector):
            red_neighbours = get_neighbours(noise_image, y, x, 2)  # red
            green_neighbours = get_neighbours(noise_image, y, x, 1)  # green
            blue_neighbours = get_neighbours(noise_image, y, x, 0)  # blue

            true_pixels_red = find_true_pixels(red_neighbours)
            true_pixels_green = find_true_pixels(green_neighbours)
            true_pixels_blue = find_true_pixels(blue_neighbours)

            if len(true_pixels_red) == 0 or len(true_pixels_green) == 0 or len(true_pixels_blue) == 0:
                new_value_r = 0 
                new_value_g = 0 
                new_value_b = 0
              
            elif len(true_pixels_red) == 1 or len(true_pixels_green) == 1 or len(true_pixels_blue) == 1:
                new_value_r = true_pixels_red[0] 
                new_value_g = true_pixels_green[0] 
                new_value_b = true_pixels_blue[0]
              
            else:
                new_value_r = math.floor(np.median(true_pixels_red))
                new_value_g = math.floor(np.median(true_pixels_green))
                new_value_b = math.floor(np.median(true_pixels_blue))

            img3[y, x] = [new_value_b, new_value_g, new_value_r]

# نمایش تصاویر
cv.imshow("main image imanieh", img)
cv.imshow("apply noise imanieh", noise_image)
cv.imshow("reduce noise imanieh", img3)
cv.waitKey(0)
cv.destroyAllWindows()
