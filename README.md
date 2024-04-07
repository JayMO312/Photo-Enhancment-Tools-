# Photo-Enhancment-Tools-
 Enhance your images with this Python toolkit! Includes color correction, histogram equalization, sharpening, old photo restoration, and upscaling (using interpolation) techniques for improved image quality. Perfect for photography, image processing, and computer vision projects.




Image Enhancement Toolkit
This Python script provides a set of image enhancement techniques to improve the quality and appearance of images. It includes functions for color correction, histogram equalization, sharpening, old photo restoration, and upscaling. These techniques can be useful for various applications such as photography, image processing, and computer vision.

Features
Color Correction: Adjusts the color balance of an image to enhance its overall appearance.
Histogram Equalization: Improves the contrast and brightness of an image by redistributing pixel intensities.
Sharpening: Enhances the sharpness and clarity of edges in an image.
Old Photo Restoration: Removes blurriness and noise from old or degraded photos.
Upscaling: Increases the size of an image while preserving details and reducing pixelation.


Installation & Usage

Clone the repository to your local machine:
git clone https://github.com/your-username/image-enhancement-toolkit.git


Install the required dependencies:
pip install -r requirements.txt


Import the script into your Python project:
import image_enhancement_toolkit as iet


Call the desired function with the input and output file paths:
input_path = "path/to/input/image.jpg"
output_path = "path/to/output/image.jpg"


# Example: Color Correction
iet.color_correction(input_path, output_path, color_factor=1.5)
Customize the parameters according to your preferences.


Functions

color_correction(input_path, output_path, color_factor=1.5): Adjusts the color balance of the input image.

histogram_equalization(input_path, output_path): Enhances the contrast and brightness of the input image using histogram equalization.

sharpen_image(input_path, output_path, strength=0.5): Applies a sharpening filter to the input image to enhance its sharpness.

restore_old_photo(input_path, output_path): Restores old or degraded photos by removing blurriness and noise.

upscale_image(input_path, output_path, scale_factor=2): Increases the size of the input image while preserving details.



Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
