# 400 -> bad request
# 422 -> unprocessable entity

class HttpUnprocessableEntityError(Exception): 
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.name = 'Unprocessable Entity'
    self.status_code = 422

try:
  print('Estou no bloco try')
  raise HttpUnprocessableEntityError('estou lancando a exception')
except Exception as exception:
  print('Estou no tratamento de erro')
  print(exception.name)
  print(exception.status_code)
  print(exception.message)