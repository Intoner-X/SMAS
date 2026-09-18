import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("Upload a JPG/PNG image")
uploaded = files.upload()
filename = list(uploaded.keys())[0]
original = cv2.imread(filename)
img = original.copy()          

def show(image, title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

show(img, "Original Image")

while True:
    print("\n---- MENU ----")
    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("0. Exit")

    choice = input("Enter choice: ")
    rows, cols = img.shape[:2]

    if choice == "1":                       # ROTATE
        angle = float(input("Enter angle (degrees): "))
        M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
        img = cv2.warpAffine(img, M, (cols, rows))
        show(img, f"Rotated by {angle} degrees")

    elif choice == "2":                     # RESIZE
        scale = float(input("Enter scale factor (e.g. 0.5, 2): "))
        img = cv2.resize(img, None, fx=scale, fy=scale)
        show(img, f"Resized by {scale}x")

    elif choice == "3":                     # FLIP
        print("1: Horizontal  0: Vertical  -1: Both")
        mode = int(input("Enter flip mode: "))
        img = cv2.flip(img, mode)
        show(img, "Flipped Image")

    elif choice == "4":                     # SHEAR
        shx = float(input("Enter shear factor X: "))
        shy = float(input("Enter shear factor Y: "))
        M = np.float32([[1, shx, 0],
                         [shy, 1, 0]])
        img = cv2.warpAffine(img, M, (cols, rows))
        show(img, "Sheared Image")

    elif choice == "5":                     # CUSTOM MATRIX
        print("Enter 6 values: a b tx c d ty (space-separated)")
        vals = list(map(float, input().split()))
        M = np.float32(vals).reshape(2, 3)
        img = cv2.warpAffine(img, M, (cols, rows))
        show(img, "Custom Matrix Transform")

    elif choice == "6":                     # RESET
        img = original.copy()
        show(img, "Reset to Original")

    elif choice == "0":                     # EXIT
        print("Exiting toolbox.")
        break

    else:
        print("Invalid choice, try again.")