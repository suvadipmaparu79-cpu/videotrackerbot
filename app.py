from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Video Tracker Running"

@app.route("/t/<track_id>")
def track(track_id):
    print(f"Clicked: {track_id}")
    return redirect("https://1024terabox.com/s/1lCVPToVChMA906byN79ERg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
