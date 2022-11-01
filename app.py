from flask import Flask
from flask import request
from flask import render_template
from os import remove
import tarfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10


@app.route('/', methods=['GET', 'POST'])
def upload_file(name=None):
    if request.method == 'POST':
        tempfile = "/tmp/upload.tar"
        f = request.files['the_file']
        f.save(tempfile)
        if not tarfile.is_tarfile(tempfile):
            return render_template('not_a_tar.html')
        a = tarfile.open(tempfile)
        if '/home/awesomeperson/important_files/cookie_clicker.txt' in a.getnames():
            remove(tempfile)
            return render_template("flag.html")
        remove(tempfile)
        return render_template("thanks.html")
    else:
        return render_template('send_me_meme_tars.html')
