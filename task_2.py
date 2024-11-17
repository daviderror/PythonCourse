import json

def calculate_weighted_score(json_file_path):
    with open(json_file_path, mode='r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)
json_file_path = 'input.json'
result = calculate_weighted_score(json_file_path)
print(result)