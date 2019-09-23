import pytest

assignment_list = {}

def createAssignment(title, points):
  assignment_list.update({title: points})
  # to fail test, replace variables title and points with the hardcoded values "" and 0

def test_create_Assignment():
  createAssignment('Assignment 5', 10)
  assert 'Assignment 5' in assignment_list
  assert assignment_list.get('Assignment 5') == 10
  
