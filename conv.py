import numpy as np
from numpy.lib.stride_tricks import as_strided

def conv2d(a, f):
    """
    This function applies 2D convolution to the input image.
    parameters:
        a: input image
        f: filter
    return:
        output: Image after applying 2D convolution
    """

    pad_h, pad_w = f.shape[0] // 2, f.shape[1] // 2
    a_padded = np.pad(a, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    s = f.shape + tuple(np.subtract(a_padded.shape, f.shape) + 1)
    subM = as_strided(a_padded, shape=s, strides=a_padded.strides * 2)

    return np.einsum('ij,ijkl->kl', f, subM)