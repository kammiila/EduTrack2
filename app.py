from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from data import GROUPS_DATA, STUDENTS_DATA, save_attendance, get_students_with_attendance, get_attendance_summary

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", groups=GROUPS_DATA)

@app.route("/students/<group_id>", methods=["GET", "POST"])
def students(group_id):
    selected_date = request.args.get("date") or date.today().isoformat()

    if request.method == "POST":
        present_ids = request.form.getlist("present_students")
        present_ids = list(map(int, present_ids))
        save_attendance(group_id, selected_date, present_ids)
        return redirect(url_for("students", group_id=group_id, date=selected_date))

    students_with_status = get_students_with_attendance(group_id, selected_date)
    return render_template("students.html",
                           group_id=group_id,
                           students=students_with_status,
                           selected_date=selected_date,
                           groups=GROUPS_DATA)

@app.route("/analysis/<group_id>")
def analysis(group_id):
    selected_date = request.args.get("date") or date.today().isoformat()
    summary = get_attendance_summary(group_id, selected_date)
    return render_template("analysis.html",
                           group_id=group_id,
                           selected_date=selected_date,
                           summary=summary,
                           groups=GROUPS_DATA)

if __name__ == "__main__":
    app.run(debug=True)
