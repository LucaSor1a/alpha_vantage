import requests
from pprint import pprint

endpoint = "https://api.estadisticasbcra.com/merval_usd"
data = {"ip": "1.1.2.3"}
headers = {"Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDg2OTU5MTYsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJsdXNjYXNvcmlhQGhvdG1haWwuY29tIn0.62h21MelBAaL3Ynqv87XnA9XYeh2D5xWFv20C_FzkNIywSUicBgtZ0dIIYrGELXKDXNLwOQzW7lm1onuQlXIjQ"}

valores = requests.get(endpoint, data=data, headers=headers).json()
pprint(valores)