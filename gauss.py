import numpy as np
from conv import conv2d

def gaussFilter(img, k, sigma):
    """
    This function applies Gaussian filter to the input image.
    parameters:
        img: input image
        k: kernel size
        sigma: standard deviation of Gaussian distribution
    return:
        filtered_image: Image after applying Gaussian filter
    """
    
    kernel = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            kernel[i, j] = np.exp(-((i - k // 2) ** 2 + (j - k // 2) ** 2) / (2 * sigma ** 2))
    kernel /= np.sum(kernel)
    
    
    filtered_image = np.zeros_like(img)
    for channel in range(3):
        filtered_image[..., channel] = conv2d(img[..., channel], kernel)
    
    return filtered_image