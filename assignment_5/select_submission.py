def select_submission(student, assignment, students, submissions):
  index = students.get(student)
  return submissions[index].get(assignment)
