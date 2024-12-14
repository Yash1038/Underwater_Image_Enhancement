from enhancement import enhancement
import cv2
import os

if __name__ == "__main__":

    input_dir = 'Input_imgs'
    output_dir = 'Output_imgs'

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            img = cv2.imread(os.path.join(input_dir, filename))
            if img is None:
                raise ValueError("Image not loaded")
            else:
                kernel_size = max(img.shape) - 1 if max(img.shape) % 2 == 0 else max(img.shape)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                enhanced_image = enhancement(img, k=kernel_size, sigma=2, clipLimit=2.0, tileGridSize=(4, 4), alpha=0.7)
                enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(output_dir, filename), enhanced_image)
        else:
            continue

    