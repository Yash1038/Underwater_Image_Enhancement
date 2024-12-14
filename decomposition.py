import numpy as np
import pandas as pd
import cv2
from gauss import gaussFilter

def decomposition(img, k = 15, sigma = 0.5):
    """
    This function applies decomposition to the input image.
    parameters:
        img: input image
        k: kernel size
        sigma: standard deviation of Gaussian distribution
    return:
        decomposed_image: Image after applying decomposition
    """
    structure = gaussFilter(img, k, sigma)
    texture = img - structure
    return structure, texture
