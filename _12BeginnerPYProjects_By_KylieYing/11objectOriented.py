
from libraries.image import Image
import numpy as np

def brighten(image, factor):
    x_pixels, y_pixels, num_channels = image.array.shape
    _image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for xp in range(x_pixels):
        for yp in range(y_pixels):
            for nc in range(num_channels):
                _image.array[xp, yp, nc] = image.array[xp, yp, nc] * factor
    
    return _image


def adjust_contrast(image, factor, mid):
    x_pixels, y_pixels, num_channels = image.array.shape
    _image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for xp in range(x_pixels):
        for yp in range(y_pixels):
            for nc in range(num_channels):
                _image.array[xp, yp, nc] = (image.array[xp, yp, nc] - mid) * factor + mid

    return _image

def blur(image, kernel_size):
    x_pixels, y_pixels, num_channels = image.array.shape
    _image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2
    
    for xp in range(x_pixels):
        for yp in range(y_pixels):
            for nc in range(num_channels):
                total = 0

                for xnr in range(max(0, xp - neighbor_range), min(x_pixels -1 , xp + neighbor_range + 1)):
                    for ynr in range(max(0, yp - neighbor_range), min(y_pixels -1 , yp + neighbor_range + 1)):
                        total = total + image.array[xnr, ynr, nc]
                _image.array[xp, yp, nc] = total / (kernel_size ** 2)

    return _image

def apply_kernel(image, kernel):
    x_pixels, y_pixels, num_channels = image.array.shape
    _image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2
    
    for xp in range(x_pixels):
        for yp in range(y_pixels):
            for nc in range(num_channels):
                total = 0

                for xnr in range(max(0, xp - neighbor_range), min(x_pixels -1 , xp + neighbor_range + 1)):
                    for ynr in range(max(0, yp - neighbor_range), min(y_pixels -1 , yp + neighbor_range + 1)):
                        x_kernel = xnr + neighbor_range - xp
                        y_kernel = ynr + neighbor_range - yp
                        kernel_value = kernel[x_kernel, y_kernel]
                        total = total + image.array[xnr, ynr, nc] * kernel_value
                _image.array[xp, yp, nc] = total

    return _image

def combine_images(image1, image2):
    x_pixels, y_pixels, num_channels = image1.array.shape
    _image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for xp in range(x_pixels):
        for yp in range(y_pixels):
            for nc in range(num_channels):
                _image.array[xp, yp, nc] = (image1.array[xp, yp, nc] ** 2 + image2.array[xp, yp, nc] ** 2) ** 0.5
    return _image

    
if __name__ == '__main__':
    lake = Image(filename='\images\lake.png')
    city = Image(filename='\images\city.png')

    brightened_image = brighten(lake, 1.7)
    brightened_image.write_image("brightened_im.png")

    darkened_image = brighten(lake, 0.3)
    darkened_image.write_image("darkened0P3.png")

    increase_contrast = adjust_contrast(lake,3, mid=0.5)
    increase_contrast.write_image("increase_contrast.png")

    decrease_contrast = adjust_contrast(lake, 0.5, mid=0.5)
    decrease_contrast.write_image("decrease05.png")

    blur_3 = blur(city, 3).write_image("blur_k3.png")
    blur_15 = blur(city, 15).write_image("blur_k15.png")

    sobel_x_kernel = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])

    sobel_y_kernel = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    sobel_x = apply_kernel(city, sobel_x_kernel)
    sobel_x.write_image("edge_x.png")
    sobel_y = apply_kernel(city, sobel_y_kernel)
    sobel_y.write_image("edge_y.png")

    sobel_combine = combine_images(sobel_x, sobel_y).write_image("final.png")