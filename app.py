from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Serve other HTML pages directly
@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(".", path)

@app.post("/contact")
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("New contact form submission:")
    print(name, email, message)

    # TODO: send email or save to database
    return "<h1>Thank you for contacting us!</h1><p>We will get back to you soon.</p>"

if __name__ == "__main__":
    app.run(debug=True)