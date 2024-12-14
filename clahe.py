import numpy as np
import cv2
import pandas as pd

def clahe(img, clipLimit=2.0, tileGridSize=(4, 4)):
    """
    This function applies CLAHE to the input image.
    parameters:
        img: input image
        clipLimit: Threshold for contrast limiting.
        tileGridSize: Size of grid for histogram equalization. Input image will be divided into equally sized rectangular tiles.

    return:
        clahe_image: Image after applying CLAHE
    """
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    clahe_img_r = clahe.apply(img[:, :, 0])
    clahe_img_g = clahe.apply(img[:, :, 1])
    clahe_img_b = clahe.apply(img[:, :, 2])
    clahe_image = cv2.merge([clahe_img_r, clahe_img_g, clahe_img_b])
    return clahe_image