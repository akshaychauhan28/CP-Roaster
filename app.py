from flask import Flask, request, jsonify, render_template
from fetcher.cf_client import fetch_profile
from analyzer.report import build_report
from roaster.llm_client import generate_roast

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():
    handle = request.json["handle"]
    profile = fetch_profile(handle)
    report = build_report(profile)
    roast_text = generate_roast(report)

    return jsonify({
    "roast": roast_text,
    "handle": report["handle"],
    "rating": report["rating"],
    "rank": report["rank"],
    "solved_count": report["solved_count"],
    "acceptance_rate": round(report["acceptance_rate"], 1),
    "avg_difficulty": round(report["avg_difficulty"], 0),
    "activity_streak": report["activity_streak"],
    "weak_areas": report["top_weak_areas"],
    "contest_count": report["contest_count"]
})

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)