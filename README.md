# Image Transformation Toolbox

A simple interactive Python tool (built for **Google Colab**) that lets you upload an image and apply common geometric transformations — Rotate, Resize, Flip, Shear, Custom Matrix, and Reset — through a menu-driven interface.

## Features

| Option | Description |
|--------|-------------|
| **1. Rotate** | Rotates the image by a user-given angle (in degrees) around its center. |
| **2. Resize** | Scales the image up or down using a scale factor (e.g., 0.5 = half size, 2 = double size). |
| **3. Flip** | Flips the image horizontally, vertically, or both. |
| **4. Shear** | Slants the image along the X and/or Y axis using shear factors. |
| **5. Custom Matrix** | Applies a user-defined 2×3 affine transformation matrix for advanced/custom transforms. |
| **6. Reset** | Restores the image to its original, unmodified state. |
| **0. Exit** | Ends the program. |

## How It Works

- **Upload:** Uses `google.colab.files.upload()` to let the user pick an image, which is then read using `cv2.imread()`.
- **Display:** The `show()` function converts the image from OpenCV's BGR color format to RGB (since `matplotlib` expects RGB) and renders it with a title.
- **Transformations:** Each menu option builds a transformation matrix (or uses a built-in OpenCV function) and applies it using `cv2.warpAffine()`, `cv2.resize()`, or `cv2.flip()`.
- **Menu Loop:** A `while True` loop keeps showing the menu and processing the user's choice until they select `0` to exit.

## Transformation Details

- **Rotate:** Uses `cv2.getRotationMatrix2D(center, angle, scale)` to build a rotation matrix, then applies it with `warpAffine`.
- **Resize:** Uses `cv2.resize()` with `fx`/`fy` scale factors.
- **Flip:** Uses `cv2.flip()` with mode `1` (horizontal), `0` (vertical), or `-1` (both).
- **Shear:** Builds a custom affine matrix:
  ```
  [1   shx   0]
  [shy  1    0]
  ```
- **Custom Matrix:** Accepts 6 user-entered values (`a b tx c d ty`) and reshapes them into a 2×3 affine matrix:
  ```
  [a   b   tx]
  [c   d   ty]
  ```

## Notes

- Transformations are applied cumulatively on the current image, not the original — use **Reset** to start over.
- No error handling is included for invalid inputs (e.g., non-numeric values), so enter parameters carefully.
- The image canvas size stays fixed during rotation/shear, so heavily rotated or sheared images may appear cropped.