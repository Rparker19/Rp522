import pytest
from grade_assignment import grade_assignment

assignments = ['Assignment', 'Another assignment', 'yet another assignment']
graded_assignments = {}

# to fail test, remove 'Assignment' from assignments list

def test_grade_assignment():
  grade_assignment('Assignment', assignments, graded_assignments)
  assert graded_assignments.get('Assignment') == pytest.approx(100)
