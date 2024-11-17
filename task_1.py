import csv
import json
from collections import OrderedDict
def csv_to_json(csv_file_path, delimiter=',', line_terminator='\n'):
    data = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            data.append(OrderedDict(row))
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    return json_data
csv_file_path = 'input.csv'
json_output = csv_to_json(csv_file_path)
print(json_output)