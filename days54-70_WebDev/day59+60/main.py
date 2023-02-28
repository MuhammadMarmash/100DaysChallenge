from flask import Flask, render_template, request
import requests
import sys

sys.path.append("/home/muhammad/python/100DaysChallenge/days32-40_api/day39_telegram/")
from notification_manager import NotificationManager

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
all_blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        try:
            if request.method == 'POST':
                data = request.form
                notificationmanager = NotificationManager()
                notificationmanager.send_telegram_message(f'Message from {data["name"]}\n'
                                                          f'Contacts: {data["email"]} {data["phone"]}\n'
                                                          f'Content: {data["message"]}')
                return render_template("contact.html", msg_sent=True)
        except KeyError:
            print("the hell??")
    return render_template("contact.html", msg_sent=False)


@app.route('/blog/<int:id>')
def the_blog(id):
    for blog in all_blogs:
        if blog["id"] == id:
            return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
