import pytest
from select_submission import select_submission

students = {"John Smith":0, "Joe Smith":1}
submissions = [{1:123, 2:456, 3:7656453423, 4:12345},
	       {1:2345, 2:765, 3:2316462, 4:00000}]

def test_selectSubmission():
  assert select_submission("John Smith", 4, students, submissions) == 12345
# to fail test, change the file number 12345 in test_selectSubmission to any other number or remove '4:12345' from submissions
