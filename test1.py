from Arrays.find_peak_element import find_peak_element
from Arrays.find_unpaired import find_unpaired_element

def test_peak():
  assert find_peak_element([1,5,3,1])==1
  
def test_unpaired():
  assert find_unpaired_element([1,5,3,4,1,5,4])==3
