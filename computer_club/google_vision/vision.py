import io
import sys
import os

from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                            'computer_club_cred.json')
client = vision.ImageAnnotatorClient()


def detect_logos(image_path):
    """Return list image detect response from Google API"""

    with io.open(image_path, 'rb') as f_img:
        content = f_img.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)
    return response.logo_annotations


if __name__ == '__main__':
    response = detect_logos(sys.argv[1])
    print('Logo, Score')
    for logo in response:
        print('{}, {}'.format(logo.description, logo.score))


def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))