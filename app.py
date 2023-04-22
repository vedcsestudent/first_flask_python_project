from flask import Flask, render_template, jsonify

app = Flask(
  __name__)  #initialize the flas constructor take the name as an argument

print(__name__)
jobs = [{
  "id": 1,
  "title": "data scientist",
  "salary": "Rs200000",
  "location": "Sanfrancisco"
}, {
  "id": 1,
  "title": "data scientist",
  "salary": "Rs2000e00",
  "location": "Sanfranciscorr"
}, {
  "id": 1,
  "title": "data scientist",
  "salary": "Rs20r0000",
  "location": "Sanfranciscor"
}, {
  "id": 1,
  "title": "data scientist",
  "salary": "Rs20r0000",
  "location": ""
}]


@app.route("/")
def hello_world():
  return render_template("home.html", company="Alpha con",
                         Jobs=jobs)  #it will render the template file


@app.route("/jobs")
def show_job():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
