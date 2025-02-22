import os
import json

json_list = []

for file_name in os.listdir("./convertedXactimateJsonFiles/"):
    converted_json = json.loads(
        open(f"./convertedXactimateJsonFiles/{file_name}", "r").read()
    )
    json_list.append(converted_json)

for json_dataset in json_list:
    
