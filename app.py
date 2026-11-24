from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def tampil_form():
    return render_template("index.html", nama="", gender="")


@app.route("/", methods=["POST"])
def index():
    nama = request.form.get("nama", "").strip()
    gender = request.form.get("gender", "")

    if not nama:
        return render_template("index.html", pesan="Masukkan nama terlebih dahulu."), 400

    return render_template("index.html", nama=nama, gender=gender)


if __name__ == "__main__":
    app.run()