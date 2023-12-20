import numpy as np
import cv2
import os

def show(img, size=1000):
    h, w = img.shape[:2]
    m = max(h, w)

    img = cv2.resize(img, (int(w/m*size), int(h/m*size)))
    cv2.imshow("image", img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

def find_file(folder_path, file_name):
    files = os.listdir(folder_path)

    for file in files:
        base_name, extension = os.path.splitext(file)
        if base_name == file_name:
            return os.path.join(folder_path, file)

    return None

def get_outline(im):
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def get_colors(im):
    pass


name = input("Name of asset (without ext): ")
path = find_file("assets/images", name)
im = cv2.imread(path)

"""
Outlines
"""

contours = get_outline(im)

# Display outlines
for i in range(-1, len(contours)):
    print(f"Contour {i}")

    blank_img = np.zeros_like(im)
    outline = cv2.drawContours(blank_img, contours, i, (0, 255, 0), 3)

    show(outline)

# Optionally remove contours
include = set(range(len(contours)))
while True:
    e = input("Exclude?: ")
    if not e: break
    include.remove(int(e))

contours = [contours[i] for i in include]

# Save
blank_img = np.zeros_like(im)
outline = cv2.drawContours(blank_img, contours, -1, (0, 255, 0), 3)
show(outline)

if input("Save? (y/n) ") == "y":
    out_path = os.path.join("assets/turtle/outlines", name + ".npz")
    np.savez(out_path, *contours)
    print("Saved")

"""
Colors
"""