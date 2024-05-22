from typing import Dict
from src.drivers.numpy_handler import NumpyHandler
from .calculator_4 import Calculator_4

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
  calculator_4 = Calculator_4(NumpyHandler())
  response = calculator_4.calculate(mock_request)
  
  assert response == {'data': {'Calculator': 4, 'Result': 3.0}}