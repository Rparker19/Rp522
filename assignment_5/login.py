def login(username, password, list):
  if username in list:
    if list.get(username) == password:
      return True
  return False
