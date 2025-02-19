from flask import Blueprint
from init import db
from models.student import Student, many_students

students_bp = Blueprint('students', __name__)

# CRUD
# read all GET/students
@students_bp.route('/students')
def get_all_student():
    # generate stmt when working with alchemy
    stmt = db.select(Student) #select Students db & put into stmt variable
    students = db.session.scalars(stmt) #pass stmt variable  to get all students
    return many_students.dump(students)
    # invoke schema
    
# read one GET/students/<int:id>
# enrol POST/students
# update PUT/students/<int:id>
# delete DELETE/students/<int:id>

# unenrol DELETE/students/<int:student_id>/int:course_id>
# create  POST/students/<int:student_id>/int:course_id>
