from flask import Flask, redirect

app = Flask(__name__)

clicks = 0

@app.route("/")
def home():
    return "Video Tracker Running"

@app.route("/t/<track_id>")
def track(track_id):
    global clicks
    clicks += 1

    print(f"Link opened: {track_id}")
    print(f"Total clicks: {clicks}")

    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
