import numpy as np
import pandas as pd
import cv2

def gray_world(img, alpha = 0.8):
    """
    This function applies Gray World algorithm to the input image.
    parameters:
        img: input image
    return:
        balanced_image: Image after applying Gray World algorithm
    """
    avg = np.mean(img, axis=(0, 1))
    avg_gray = np.mean(avg)
    alpha = alpha
    balanced_image = np.zeros_like(img)
    for channel in range(3):
        balanced_image[..., channel] = img[..., channel] * (avg_gray / avg[channel])
    balanced_image[..., 0] = alpha * balanced_image[..., 0]
    return balanced_image