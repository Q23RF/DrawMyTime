from flask import Flask, render_template, request, url_for
from PIL import Image
import functions

app = Flask(__name__)
albums = ['sticky','sticker','hello','future','stranger','hitchhiker','diary','hide','i-love-jc','ver1','ver2','xxB','BlueHourR','attacca1','MicOnMain','BlueBlastJC','fallen','t-crush','tearU','holidayM']

	


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


    else:
        img_list = [url_for('static',filename='blank.jpg')]
    return render_template('main.html',pcs=img_list, banner=url_for('static',filename='banner.jpg'))
		
@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        fb = request.form["fb"]
        functions.send_line(fb)
    return render_template('feedback.html')

	
app.run(host='0.0.0.0', port=81)