import pytest
from login import login

username_list = {
  'username':'password',
  'software_engineer_100':'123456789',
  'johnsmith':'generic_password'
  } 

def test_login():
  assert login('username', 'password', username_list)
# to fail test, change variables in login function call to a combination that does not appear in username_list, such as 'myname', 'mypassword'

