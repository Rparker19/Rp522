import pytest

username_list = {
  'username':'password',
  'software_engineer_100':'123456789',
  'johnsmith':'generic_password'
  } 

def login(username, password):
  if username in username_list:
    if username_list.get(username) == password:
      return True
  return False

def test_login():
  assert login('username', 'password')
# to fail test, change variables in login function call to a combination that does not appear in username_list

