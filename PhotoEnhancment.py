import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os


def color_correction(input_path, output_path, color_factor=1.5):
    print("Applying color correction...")
    image = Image.open(input_path)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(color_factor)
    image.save(output_path)
    print(f"Color correction applied. Saved at {output_path}")


def histogram_equalization(input_path, output_path):
    print("Applying histogram equalization...")
    image = cv2.imread(input_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)
    enhanced_image = cv2.merge([equalized_image] * 3)
    cv2.imwrite(output_path, cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR))
    print(f"Histogram equalization applied. Saved at {output_path}")


def sharpen_image(input_path, output_path, strength=0.5, contrast_factor=1.2, saturation_factor=1.2):
    print("Applying sharpening...")
    image = cv2.imread(input_path)

    sharpening_filter = np.array([[-1, -1, -1],
                                  [-1, 9 + strength, -1.5],
                                  [-1, -1, -1]])

    # Apply the filter
    sharpened_image = cv2.filter2D(image, -1, sharpening_filter)

    # Ensure pixel values are within the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255)

    # Enhance contrast and saturation
    sharpened_image = cv2.convertScaleAbs(sharpened_image, alpha=contrast_factor, beta=0)
    sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2HSV)
    sharpened_image[:, :, 1] = np.clip(sharpened_image[:, :, 1] * saturation_factor, 0.8, 255)
    sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_HSV2BGR)

    # Save the result
    cv2.imwrite(output_path, sharpened_image)
    print(f"Sharpening applied. Saved at {output_path}")


def restore_old_photo(input_path, output_path):
    print("Restoring old photo...")
    enhanced_image = cv2.imread(input_path, cv2.IMREAD_COLOR)

    # Apply deblurring (Wiener deconvolution example)
    enhanced_image = wiener_deconvolution(enhanced_image)

    cv2.imwrite(output_path, enhanced_image)
    print(f"Old photo restored. Saved at {output_path}")


def upscale_image(input_path, output_path, scale_factor=2):
    print(f"Upscaling image by a factor of {scale_factor}...")
    image = cv2.imread(input_path)
    upscaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output_path, upscaled_image)
    print(f"Upscaling applied. Saved at {output_path}")


def wiener_deconvolution(image, kernel_size=(5, 5), noise_var=0.1):

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Add Gaussian noise
    noise = np.random.normal(0, noise_var, gray_image.shape)
    noisy_image = gray_image + noise

    # Apply Wiener deconvolution
    kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
    deblurred_image = cv2.filter2D(noisy_image, -1, kernel)

    return deblurred_image


input_image_path = "C:\\Users\\jonat\\PycharmProjects\\pythonProject(new)\\Enhancments\\Dragon1.jpeg"
output_directory = "C:\\path\\to\\your\\output\\"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Color Correction
color_correction(input_image_path, os.path.join(output_directory, "color_corrected_image.jpg"), color_factor=1.5)

# Histogram Equalization
histogram_equalization(input_image_path, os.path.join(output_directory, "histogram_equalized_image.jpg"))

# Sharpening
sharpen_image(input_image_path, os.path.join(output_directory, "sharpened_image.jpg"), strength=-0.1)

# Old Photo Restoration (Wiener deconvolution)
restore_old_photo(input_image_path, os.path.join(output_directory, "restored_old_photo.jpg"))

# Upscaling
upscale_image(input_image_path, os.path.join(output_directory, "upscaled_image.jpg"), scale_factor=2)
