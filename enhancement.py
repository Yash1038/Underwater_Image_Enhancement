from clahe import clahe
from gray_world import gray_world
from attenuation import attenuation
from decomposition import decomposition

def enhancement(img, k = 15, sigma = 0.5, clipLimit=2.0, tileGridSize=(4, 4), alpha = 0.8):
    """
    This function applies enhancement to the input image.
    parameters:
        img: input image
        k: kernel size
        sigma: standard deviation of Gaussian distribution
        clipLimit: Threshold for contrast limiting.
        tileGridSize: Size of grid for histogram equalization. Input image will be divided into equally sized rectangular tiles.
        alpha: parameter for Gray World algorithm
    return:
        enhanced_image: Image after applying enhancement
    """
    clahe_image = clahe(img, clipLimit, tileGridSize)
    structure, texture = decomposition(clahe_image, k, sigma)
    attenuation_image = attenuation(texture, structure)
    enhanced_image = gray_world(attenuation_image, alpha)
    return enhanced_image

    