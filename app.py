from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None  # Initialize the QR path variable
    if request.method == "POST":
        # Retrieve form data
        name_book = request.form.get("name_book")
        name_author = request.form.get("name_author")
        qty = request.form.get("qty")
        price = request.form.get("price")
        cat = request.form.get("cat")

        # Combine inputs into a single string
        string = f"{name_book}|{name_author}|{qty}|{price}|{cat}"

        # Generate QR code
        qr = qrcode.make(string)
        qr_filename = "myqr.png"
        qr_path = os.path.join("static", qr_filename)
        qr.save(qr_path)  # Save the QR code in the static folder

        # Update the path to be accessible by the browser
        qr_path = f"/static/{qr_filename}"
        
    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(debug=True)
