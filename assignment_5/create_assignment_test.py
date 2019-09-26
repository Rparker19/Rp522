import pytest
from create_assignment import create_assignment

def test_create_Assignment():
  assignment_list = {}
  create_assignment('Assignment 5', 10, assignment_list)
  assert 'Assignment 5' in assignment_list # to fail, assert 'Assignment' in assignment_list
  assert assignment_list.get('Assignment 5') == 10 # to fail, assert ...==12
  
