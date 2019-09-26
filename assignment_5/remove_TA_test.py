import pytest
from remove_TA import remove_TA

def test_remove_TA():
  TA_list = ["TA 1", "TA 2"]
  remove_TA("TA 2", TA_list) # to fail: remove_TA("TA 1", TA_list)
  assert "TA 2" not in TA_list 

