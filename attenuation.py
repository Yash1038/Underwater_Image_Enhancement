import numpy as np
import pandas as pd
import cv2

def attenuation(texture, structure):
    """
    This function applies R channel attenuation to the input image.
    parameters:
        texture: texture image
        structure: structure image
    return:
        attenuated_image: Image after applying attenuation
    """
    avg_green = np.mean(texture[..., 1])
    avg_blue = np.mean(texture[..., 2])
    
    if avg_green > avg_blue:
        texture[:,:,0] = texture[:,:,1]
    else:
        texture[:,:,0] = texture[:,:,2]

    final = texture + structure
    return final