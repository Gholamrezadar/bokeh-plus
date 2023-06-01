import cv2
import numpy as np
import argparse
from pathlib import Path

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Bokeh effect')
    parser.add_argument('input', type=str, help='Input image')
    parser.add_argument('kernel', type=str, help='Kernel image')
    parser.add_argument('output', type=str, help='Output image')
    parser.add_argument('--kernel_size', type=int, default=32, help='Kernel size')
    args = parser.parse_args()

    # Get the paths
    img_path = Path(args.input)
    kernel_path = Path(args.kernel)
    out_path = Path(args.output)

    # Open the image
    img = cv2.imread(str(img_path))
    kernel = cv2.imread(str(kernel_path))

    # Resize the kernel
    if args.kernel_size < 3:
        print("Kernel size must be greater than 3")
        exit()

    # resize the kernel
    kernel = cv2.resize(kernel, (args.kernel_size, args.kernel_size))

    # Convert to float32 between 0-1
    img = img.astype('float32') / 255.0
    kernel = kernel.astype('float32') / 255.0

    # img = img ** 4
    # Inverse Tone mapping
    contrast = 1.0
    print("before inverse tonemapping", np.min(img), np.max(img))
    img = (img/contrast) / (1.0 - img + 0.0000000001)
    print("after inverse tonemapping", np.min(img), np.max(img))

    # Convolve with a kernel image
    kernel_size = args.kernel_size
    img = cv2.filter2D(img, -1, kernel)
    img /= kernel_size * kernel_size * 0.4015  # total sum of the kernel
    print("after filter: ", np.min(img), np.max(img))

    # Tone mapping
    img = contrast*img / (contrast*img + 1.0)
    print("after tonemapping", np.min(img), np.max(img))

    print(np.min(img), np.max(img))

    # Save the image
    img = (img * 255.0).astype('uint8')
    cv2.imwrite(str(out_path), img)

    cv2.destroyAllWindows()
