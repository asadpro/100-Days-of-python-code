import requests

# Below get method will get data in json format and then at last the text keyword will get only the text out of that json file. Now json_data variable contain json file
json_data = requests.get(
    "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
).text


# To convert this json file into a python dictionary we need json module or we can use json keyword to replace the above text keyword
import json

actual_data = json.loads(json_data)
del actual_data["response_code"]

# print(actual_data['results'][0]['question'])
# print(actual_data['results'][0]['correct_answer'])
