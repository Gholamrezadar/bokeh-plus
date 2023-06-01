import cv2
import numpy as np
import argparse
from pathlib import Path
from numba import njit, jit

@njit
def gen_points(radius):
    multipliers = [2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]
    offsets = np.array([
        [1.000000, 0.000000],
        [0.707107, 0.707107],
        [-0.000000, 1.000000],
        [-0.707107, 0.707107],
        [-1.000000, -0.000000],
        [-0.707106, -0.707107],
        [0.000000, -1.000000],
        [0.707107, -0.707107],
        [1.000000, 0.000000],
        [0.923880, 0.382683],
        [0.707107, 0.707107],
        [0.382683, 0.923880],
        [-0.000000, 1.000000],
        [-0.382684, 0.923879],
        [-0.707107, 0.707107],
        [-0.923880, 0.382683],
        [-1.000000, -0.000000],
        [-0.923879, -0.382684],
        [-0.707106, -0.707107],
        [-0.382683, -0.923880],
        [0.000000, -1.000000],
        [0.382684, -0.923879],
        [0.707107, -0.707107],
        [0.923880, -0.382683],
        [1.000000, 0.000000],
        [0.965926, 0.258819],
        [0.866025, 0.500000],
        [0.707107, 0.707107],
        [0.500000, 0.866026],
        [0.258819, 0.965926],
        [-0.000000, 1.000000],
        [-0.258819, 0.965926],
        [-0.500000, 0.866025],
        [-0.707107, 0.707107],
        [-0.866026, 0.500000],
        [-0.965926, 0.258819],
        [-1.000000, -0.000000],
        [-0.965926, -0.258820],
        [-0.866025, -0.500000],
        [-0.707106, -0.707107],
        [-0.499999, -0.866026],
        [-0.258819, -0.965926],
        [0.000000, -1.000000],
        [0.258819, -0.965926],
        [0.500000, -0.866025],
        [0.707107, -0.707107],
        [0.866026, -0.499999],
        [0.965926, -0.258818],
    ])
    for i in range(offsets.shape[0]):
        offsets[i] *= multipliers[i] * radius
    return offsets

@njit
def customFilter(img):
    offsets = gen_points(radius=1.0)
    result = np.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            total_weight = np.max(img[i,j])
            for offset in offsets:
                x = int(i + offset[0])
                y = int(j + offset[1])
                if 0 <= x < img.shape[0] and 0 <= y < img.shape[1]:
                    # brightness = np.max(img[x,y])
                    total_weight += 1 

                    result[i, j] += img[x, y] 
            result[i, j] /= total_weight

    return result

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Bokeh effect')
    #positional argument input
    parser.add_argument('input', type=str, help='Input image')
    parser.add_argument('output', type=str, help='Output image')
    args = parser.parse_args()

    # Get the paths
    img_path = Path(args.input)
    out_path = Path(args.output)

    
    # Open the image
    img = cv2.imread(str(img_path))

    # Resize the image
    # img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = img_gray.astype('float32')/255.0

    # Convert to float32 between 0-1
    img = img.astype('float32') / 255.0

    # Inverse Tone mapping
    contrast = 1.0
    print("before inverse tonemapping", np.min(img), np.max(img))
    img = (img/contrast) / (1.0 - img + 0.0000000001)
    print("after inverse tonemapping", np.min(img), np.max(img))

    # Convolve with a kernel image
    # img = cv2.filter2D(img, -1, kernel)
    # img /= kernel_size * kernel_size * 0.4015
    # print("after filter: ", np.min(img), np.max(img))

    img = customFilter(img)
    print("after filter: ", np.min(img), np.max(img))

    # Tone mapping
    img = contrast*img / (contrast*img + 1.0)
    print("after tonemapping", np.min(img), np.max(img))

    print(np.min(img), np.max(img))

    # Save the image
    img = (img * 255.0).astype('uint8')
    cv2.imwrite(str(out_path), img) 

    cv2.destroyAllWindows()