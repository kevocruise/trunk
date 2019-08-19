import os
import vision
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape
from werkzeug.utils import secure_filename


this_dir = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_folder=os.path.join(this_dir, 'static'))

env = Environment(
    loader=FileSystemLoader(os.path.join(this_dir, 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)


def get_past_uploads(path_to_uploads):
    """Return a list of past uploads"""

    if os.path.exists(os.path.join(path_to_uploads, 'approved.txt')):
        with open(os.path.join(path_to_uploads, 'approved.txt')) as f_approved:
            approved_uploads = f_approved.readlines()

        approved_uploads = [x.strip() for x in approved_uploads]

    else:
        return []

    past_uploads = []
    for upload in os.listdir(path_to_uploads):
        if upload in approved_uploads:
            past_uploads.append(os.path.join('static', upload))

    return past_uploads


@app.route('/', methods=['GET', 'POST'])
def index():
    template = env.get_template('index.html')
    past_uploads = get_past_uploads(app.static_folder)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)

        img_path = os.path.join(app.static_folder, filename)
        if not os.path.exists(img_path):
            file.save(img_path)

        logos = vision.detect_logos(img_path)
        vision.localize_objects(img_path)

        return template.render(image=os.path.join('static', os.path.split(img_path)[-1]),
                               results=logos,
                               past_uploads=past_uploads)

    return template.render(past_uploads=past_uploads)


if __name__ == '__main__':
    app.run(debug=True)
