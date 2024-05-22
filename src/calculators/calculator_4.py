from typing import List, Dict
from flask  import request as FlaskRequest  
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator_4:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler
  
  def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    median = self.__calculate_median(input_data)

    formated_response = self.__format_response(median)
    return formated_response

    
  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("Body mal formatado")
    
    input_data = body["numbers"]
    return input_data
  
  def __calculate_median(self, number: List[float]) -> float:
    median = self.__driver_handler.median(number)
    return median
  
  def __format_response(self, median: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "Result": median
      }
    }
