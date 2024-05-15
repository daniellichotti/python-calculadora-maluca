from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator_3


class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandlerError:
  def variance(self, numbers: List[float]) -> float:
    return 3
  
class MockDriverHandler:
  def variance(self, numbers: List[float]) -> float:
    return 1000000

def test_calculate():
  mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
  calculator_3 = Calculator_3(MockDriverHandler())

  response = calculator_3.calculate(mock_request)

  assert response == {'data': {'Calculator': 3, 'value': 1000000, 'Success': True}}
  
  

def test_calculate_with_variance_error():
  mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
  calculator_3 = Calculator_3(MockDriverHandlerError())

  with raises(Exception) as excinfo:
    calculator_3.calculate(mock_request)
  
  assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação.'