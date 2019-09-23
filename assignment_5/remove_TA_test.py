import pytest

def remove_TA(name, list):
  list.remove(name)
  # to fail test, change .remove(name) to .append(name)
def test_remove_TA():
  TA_list = ["TA 1", "TA 2"]
  remove_TA("TA 2", TA_list)
  assert "TA 2" not in TA_list


