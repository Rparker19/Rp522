def grade_assignment(title, assignments, graded_assignments):
  if title in assignments:
    graded_assignments.update({title: 100.00})
