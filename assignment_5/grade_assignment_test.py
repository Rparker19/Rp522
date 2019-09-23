import pytest

assignments = ['Assignment', 'Another assignment', 'yet another assignment']
graded_assignments = {}

def grade_assignment(title):
  if title in assignments:
    graded_assignments.update( {title : 100.00} )

# to fail test, remove 'Assignment' from assignments list

def test_grade_assignment():
  grade_assignment('Assignment')
  assert graded_assignments.get('Assignment') == pytest.approx(100)
