from flask import Flask, render_template, request, url_for
from PIL import Image
import functions

app = Flask(__name__)
albums = ['sticky','sticker','hello','future','stranger','hitchhiker']

	


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        n = int(request.form["n"])
        list = functions.all_fn(albums[n])
        pn = functions.draw_card(list, albums[n])

        pc = Image.open(pn)
        pc.save('static/pc.jpg')
        if "Hendery" in pn:
            return render_template('main.html', banner=url_for('static',filename='hbanner.jpg'), img=url_for('static',filename='pc.jpg'))
        else:
            return render_template('main.html', banner=url_for('static',filename='banner.jpg'), img=url_for('static',filename='pc.jpg'))
    else:
            return render_template('main.html', banner=url_for('static',filename='banner.jpg'))
		


	
app.run(host='0.0.0.0', port=81)





