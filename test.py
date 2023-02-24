from Math.odd_sum import odd_sum
from Math.prime_factors import prime_factors

def test_odd():
  assert odd_sum(1,3)==4
  
def test_prime():
  assert prime_factors(50)==[2,5,5]


