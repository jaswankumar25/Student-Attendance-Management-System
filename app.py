from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


# =========================================================
# MYSQL DATABASE CONNECTION
# =========================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2508",
    database="student_attendance"
)


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/")
def home():

    cursor = db.cursor()

    # -----------------------------------------------------
    # Total Students
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM students
    """)

    total_students = cursor.fetchone()[0]


    # -----------------------------------------------------
    # Total Subjects
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM subjects
    """)

    total_subjects = cursor.fetchone()[0]


    # -----------------------------------------------------
    # Students Present Today
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(DISTINCT student_id)
        FROM attendance
        WHERE attendance_date = CURDATE()
        AND status = 'Present'
    """)

    present_today = cursor.fetchone()[0]


    # -----------------------------------------------------
    # Overall Attendance Percentage
    # -----------------------------------------------------

    cursor.execute("""
        SELECT
            ROUND(
                SUM(status = 'Present') * 100.0 /
                COUNT(*),
                2
            )
        FROM attendance
    """)

    average_attendance = cursor.fetchone()[0]

    if average_attendance is None:
        average_attendance = 0


    # -----------------------------------------------------
    # Get All Students
    # -----------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    cursor.close()


    return render_template(
        "index.html",
        students=students,
        total_students=total_students,
        total_subjects=total_subjects,
        present_today=present_today,
        average_attendance=average_attendance
    )


# =========================================================
# STUDENTS PAGE
# =========================================================

@app.route("/students")
def students_page():

    cursor = db.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    cursor.close()


    return render_template(
        "students.html",
        students=students
    )


# =========================================================
# ADD STUDENT
# =========================================================

@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = request.form["student_id"].strip()
        name = request.form["name"].strip()
        department = request.form["department"].strip()
        year = request.form["year"].strip()

        cursor = db.cursor()

        try:

            # -------------------------------------------------
            # Check Duplicate Student ID
            # -------------------------------------------------

            cursor.execute("""
                SELECT student_id
                FROM students
                WHERE student_id = %s
            """, (student_id,))

            existing_student = cursor.fetchone()

            if existing_student:

                return render_template(
                    "add_student.html",
                    error=f"Student ID {student_id} already exists."
                )


            # -------------------------------------------------
            # Insert New Student
            # -------------------------------------------------

            cursor.execute("""
                INSERT INTO students
                (
                    student_id,
                    name,
                    department,
                    year
                )
                VALUES (%s, %s, %s, %s)
            """, (
                student_id,
                name,
                department,
                year
            ))

            db.commit()

            return redirect("/students")


        except mysql.connector.Error as error:

            db.rollback()

            print("Error adding student:", error)

            return render_template(
                "add_student.html",
                error="Unable to add student. Please check the entered details."
            )


        finally:

            cursor.close()


    return render_template("add_student.html")


# =========================================================
# EDIT STUDENT
# =========================================================

@app.route("/edit-student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    cursor = db.cursor()


    # -----------------------------------------------------
    # Get Existing Student
    # -----------------------------------------------------

    cursor.execute("""
        SELECT
            student_id,
            name,
            department,
            year
        FROM students
        WHERE student_id = %s
    """, (student_id,))

    student = cursor.fetchone()


    # -----------------------------------------------------
    # Student Not Found
    # -----------------------------------------------------

    if student is None:

        cursor.close()

        return "Student not found", 404


    # -----------------------------------------------------
    # Update Student
    # -----------------------------------------------------

    if request.method == "POST":

        name = request.form["name"].strip()
        department = request.form["department"].strip()
        year = request.form["year"].strip()


        cursor.execute("""
            UPDATE students
            SET
                name = %s,
                department = %s,
                year = %s
            WHERE student_id = %s
        """, (
            name,
            department,
            year,
            student_id
        ))


        db.commit()

        cursor.close()

        return redirect("/students")


    # -----------------------------------------------------
    # Open Edit Page
    # -----------------------------------------------------

    cursor.close()


    return render_template(
        "edit_student.html",
        student=student
    )


# =========================================================
# DELETE STUDENT
# =========================================================

@app.route("/delete-student/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    cursor = db.cursor()

    try:

        # -------------------------------------------------
        # Delete Attendance Records First
        # -------------------------------------------------

        cursor.execute("""
            DELETE FROM attendance
            WHERE student_id = %s
        """, (student_id,))


        # -------------------------------------------------
        # Delete Student
        # -------------------------------------------------

        cursor.execute("""
            DELETE FROM students
            WHERE student_id = %s
        """, (student_id,))


        db.commit()


    except mysql.connector.Error as error:

        db.rollback()

        print("Error deleting student:", error)


    finally:

        cursor.close()


    return redirect("/students")


# =========================================================
# SUBJECTS PAGE
# =========================================================

@app.route("/subjects")
def subjects_page():

    cursor = db.cursor()

    cursor.execute("""
        SELECT *
        FROM subjects
        ORDER BY subject_id
    """)

    subjects = cursor.fetchall()

    cursor.close()


    return render_template(
        "subjects.html",
        subjects=subjects
    )


# =========================================================
# ADD SUBJECT
# =========================================================

@app.route("/add-subject", methods=["GET", "POST"])
def add_subject():

    if request.method == "POST":

        subject_id = request.form["subject_id"].strip()
        subject_name = request.form["subject_name"].strip()

        cursor = db.cursor()

        try:

            # -------------------------------------------------
            # Check Duplicate Subject ID
            # -------------------------------------------------

            cursor.execute("""
                SELECT subject_id
                FROM subjects
                WHERE subject_id = %s
            """, (subject_id,))

            existing_subject = cursor.fetchone()

            if existing_subject:

                return render_template(
                    "add_subject.html",
                    error=f"Subject ID {subject_id} already exists."
                )


            # -------------------------------------------------
            # Insert Subject
            # -------------------------------------------------

            cursor.execute("""
                INSERT INTO subjects
                (
                    subject_id,
                    subject_name
                )
                VALUES (%s, %s)
            """, (
                subject_id,
                subject_name
            ))


            db.commit()

            return redirect("/subjects")


        except mysql.connector.Error as error:

            db.rollback()

            print("Error adding subject:", error)

            return render_template(
                "add_subject.html",
                error="Unable to add subject. Please check the entered details."
            )


        finally:

            cursor.close()


    return render_template("add_subject.html")


# =========================================================
# ATTENDANCE PAGE
# =========================================================

@app.route("/attendance")
def attendance_page():

    cursor = db.cursor()


    # -----------------------------------------------------
    # Get Filter Values From URL
    # -----------------------------------------------------

    search = request.args.get(
        "search",
        ""
    ).strip()


    subject_id = request.args.get(
        "subject_id",
        ""
    )


    attendance_date = request.args.get(
        "attendance_date",
        ""
    )


    # -----------------------------------------------------
    # Get All Students
    # -----------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()


    # -----------------------------------------------------
    # Get All Subjects
    # -----------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM subjects
        ORDER BY subject_id
    """)

    subjects = cursor.fetchall()


    # -----------------------------------------------------
    # Base Attendance Query
    # -----------------------------------------------------

    query = """
        SELECT
            attendance.attendance_id,
            students.student_id,
            students.name,
            subjects.subject_name,
            attendance.attendance_date,
            attendance.status

        FROM attendance

        JOIN students
            ON attendance.student_id = students.student_id

        JOIN subjects
            ON attendance.subject_id = subjects.subject_id

        WHERE 1 = 1
    """


    params = []


    # -----------------------------------------------------
    # Search By Student Name
    # -----------------------------------------------------

    if search:

        query += """
            AND students.name LIKE %s
        """

        params.append(
            "%" + search + "%"
        )


    # -----------------------------------------------------
    # Filter By Subject
    # -----------------------------------------------------

    if subject_id:

        query += """
            AND attendance.subject_id = %s
        """

        params.append(subject_id)


    # -----------------------------------------------------
    # Filter By Date
    # -----------------------------------------------------

    if attendance_date:

        query += """
            AND attendance.attendance_date = %s
        """

        params.append(attendance_date)


    # -----------------------------------------------------
    # Latest Attendance Records First
    # -----------------------------------------------------

    query += """
        ORDER BY
            attendance.attendance_date DESC,
            attendance.attendance_id DESC
    """


    cursor.execute(
        query,
        params
    )


    attendance_records = cursor.fetchall()


    cursor.close()


    return render_template(
        "attendance.html",
        students=students,
        subjects=subjects,
        attendance_records=attendance_records,
        search=search,
        selected_subject=subject_id,
        selected_date=attendance_date
    )


# =========================================================
# REPORTS PAGE
# =========================================================

@app.route("/reports")
def reports_page():

    cursor = db.cursor()


    cursor.execute("""
        SELECT

            students.student_id,

            students.name,

            COUNT(
                attendance.attendance_id
            ) AS total_classes,

            COALESCE(
                SUM(
                    attendance.status = 'Present'
                ),
                0
            ) AS present_classes,

            COALESCE(
                SUM(
                    attendance.status = 'Absent'
                ),
                0
            ) AS absent_classes,

            COALESCE(
                ROUND(
                    SUM(
                        attendance.status = 'Present'
                    ) * 100.0
                    /
                    NULLIF(
                        COUNT(
                            attendance.attendance_id
                        ),
                        0
                    ),
                    2
                ),
                0
            ) AS attendance_percentage


        FROM students


        LEFT JOIN attendance

            ON students.student_id =
               attendance.student_id


        GROUP BY

            students.student_id,
            students.name


        ORDER BY

            students.student_id
    """)


    reports = cursor.fetchall()


    cursor.close()


    return render_template(
        "reports.html",
        reports=reports
    )


# =========================================================
# MARK / UPDATE ATTENDANCE
# =========================================================

@app.route(
    "/mark-attendance",
    methods=["POST"]
)
def mark_attendance():

    student_id = request.form["student_id"]

    subject_id = request.form["subject_id"]

    attendance_date = request.form[
        "attendance_date"
    ]

    status = request.form["status"]


    cursor = db.cursor()


    try:

        # -------------------------------------------------
        # Check Existing Attendance
        # -------------------------------------------------

        cursor.execute("""
            SELECT attendance_id
            FROM attendance
            WHERE student_id = %s
            AND subject_id = %s
            AND attendance_date = %s
        """, (
            student_id,
            subject_id,
            attendance_date
        ))


        existing_record = cursor.fetchone()


        # -------------------------------------------------
        # Update Existing Attendance
        # -------------------------------------------------

        if existing_record:

            cursor.execute("""
                UPDATE attendance
                SET status = %s
                WHERE attendance_id = %s
            """, (
                status,
                existing_record[0]
            ))


        # -------------------------------------------------
        # Insert New Attendance
        # -------------------------------------------------

        else:

            cursor.execute("""
                INSERT INTO attendance
                (
                    student_id,
                    subject_id,
                    attendance_date,
                    status
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s
                )
            """, (
                student_id,
                subject_id,
                attendance_date,
                status
            ))


        db.commit()


    except mysql.connector.Error as error:

        db.rollback()

        print("Error marking attendance:", error)


    finally:

        cursor.close()


    return redirect("/attendance")


# =========================================================
# RUN FLASK APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True) 