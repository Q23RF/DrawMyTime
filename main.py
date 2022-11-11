from flask import Flask, render_template, request, url_for
from PIL import Image
import functions

app = Flask(__name__)
albums = ['sticky','sticker','hello','future','stranger','hitchhiker','diary']

	


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        n = int(request.form["n"])
        d_list = functions.all_dn(albums[n])
        img_list = []
        for dn in d_list:
            f_list = functions.all_fn(albums[n], dn)
            pn = functions.draw_card(f_list, albums[n], dn)
            pc = Image.open(pn)
            pc.save('static/{}.jpg'.format(dn))
            img_list.append(url_for('static',filename='{}.jpg'.format(dn)))
        return render_template('main.html',img=img_list, banner=url_for('static',filename='banner.jpg'))

    else:
            return render_template('main.html', banner=url_for('static',filename='banner.jpg'))
		


	
app.run(host='0.0.0.0', port=81)