from enhancement import enhancement
import cv2

if __name__ == "__main__":
    img = cv2.imread('Input_imgs/test1.png')
    if img is None:
        raise ValueError("Image not loaded")
    else:
        kernel_size = max(img.shape) - 1 if max(img.shape) % 2 == 0 else max(img.shape)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        enhanced_image = enhancement(img, k=kernel_size, sigma=2, clipLimit=2.0, tileGridSize=(4, 4), alpha=0.7)
        enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite('Output_imgs/test1.png', enhanced_image)