from .calculator_1 import Calculator_1
from typing import Dict

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={"number": 1})
  calculator1 = Calculator_1()

  response = calculator1.calculate(mock_request)
  
  #testar formato da resposta
  assert "data" in response
  assert "Calculator" in response["data"]
  assert "Result" in response["data"]

  #testar assertividade da resposta
  assert response["data"]["Calculator"] == 1
  assert response["data"]["Result"] == 14.25