from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator_1():
  def calculate(self, request: FlaskRequest) -> Dict:  #type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    splited_number = input_data / 3 
    
    fist_process_result = self.__first_process(splited_number)
    second_process_reault = self.__second_process(splited_number)
    calc_result = fist_process_result + second_process_reault + splited_number
    response = self.__format_response(calc_result)
    return response




  def __validate_body(self, body: Dict) -> float:
    if "number" not in body:
      raise HttpUnprocessableEntityError("body mal formatado")
    
    input_data = body["number"]
    return input_data

  def __first_process(self, first_number: float) -> float:
    first_part = (first_number /4) + 7
    second_part = (first_part**2)*0.257
    return second_part
  
  def __second_process(self, second_number: float) -> float:
    first_part = (second_number ** 2.121)
    second_part = (first_part / 5) + 1
    return second_part
  
  def __format_response(self, calc_result: float) -> Dict:
    return {
      "data": {
        "Calculator": 1,
        "Result": round(calc_result, 2)
      }
    }