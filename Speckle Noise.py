#mohammah imanieh speckle noise
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

def apply_speckle_noise(img2, width, height, noise_percentage):
    mean = 0
    variance = 0.04
    sigma = variance**0.5
    gauss = np.random.normal(mean, sigma, (height, width, 3))
    gauss = gauss.reshape(height, width, 3)
    noisy = img2 + img2 * gauss * noise_percentage / 100
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)  # اطمینان از اینکه مقادیر در محدوده 0 تا 255 باقی بمانند
    return noisy

noise_image = apply_speckle_noise(img2, width, height, noise_percentage)

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
    return [val for val in vector]

for y in range(1, height - 1):
    for x in range(1, width - 1):
        vector = noise_image[y, x]
        
        red_neighbours = get_neighbours(noise_image, y, x, 2)  # red
        green_neighbours = get_neighbours(noise_image, y, x, 1)  # green
        blue_neighbours = get_neighbours(noise_image, y, x, 0)  # blue

        true_pixels_red = find_true_pixels(red_neighbours)
        true_pixels_green = find_true_pixels(green_neighbours)
        true_pixels_blue = find_true_pixels(blue_neighbours)

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
