from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator_1

calc_route_bp = Blueprint("calc_route", __name__)

@calc_route_bp.route("/calculator/1", methods=['POST'])
def calculator_1():
  calc = Calculator_1()
  response = calc.calculate(request)

  return jsonify(response), 200