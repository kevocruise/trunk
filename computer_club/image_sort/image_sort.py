import os
import sys
from shutil import copyfile
from PIL import Image
from pprint import pprint as pp


EXTENSIONS = ['.jpg', '.png', '.jpeg']


def get_image_data(image_dir):
    images = []
    for image_file in os.listdir(image_dir):
        image_file_abspath = os.path.join(image_dir, image_file)
        if not os.path.isfile(image_file_abspath):
            continue

        name, ext = os.path.splitext(image_file)

        if ext not in EXTENSIONS:
            continue

        im = Image.open(image_file_abspath)
        width, height = im.size

        images.append({
            'name': image_file,
            'path': image_file_abspath,
            'width': width,
            'height': height,
            })

    return images


def cleanup_image(image, min_width=1000, min_height=1000):
    if image['width'] < min_width or image['height'] < min_height:
        print(f"Deleting {image['path']}, {image['width']}, {image['height']}")
        os.remove(image['path'])

    return


def image_resolution_sort(images, image_dir):
    sizes = {
        '4K': [],
        '2K': [],
        '1080p': [],
        'weird': [],
    }
    for image in images:
        # 4K
        if image['width'] >= 3840 and image['height'] >= 2160:
            sizes['4K'].append(image)

        # 2K
        elif image['width'] >= 2560 and image['height'] >= 1440:
            sizes['2K'].append(image)

        # 1080p
        elif image['width'] >= 1920 and image['height'] >= 1080:
            sizes['1080p'].append(image)

        # weird size
        else:
            sizes['weird'].append(image)

    for size in sizes:
        size_dir = os.path.join(image_dir, size)
        if not os.path.exists(size_dir):
            os.makedirs(size_dir)

        for image in sizes[size]:
            copyfile(image['path'], os.path.join(size_dir, image['name']))

    return


def main(image_dir):
    image_resolution_sort(get_image_data(image_dir), image_dir)


if __name__ == "__main__":
    main(sys.argv[1])
