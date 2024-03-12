import json, csv, re

json_path = 'logs.json'
csv_path = 'error_info.csv'

with open(json_path) as inputFile:
    content = json.load(inputFile)
    # print(content)
    pattern = r'(?i)error'
    filtered_content = [{key:value for key,value in item.items() if re.search(pattern.lower(), value)} for item in content]
    # print(filtered_content)
    
    with open(csv_path, 'w', newline='') as outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=filtered_content[0].keys())
        writer.writeheader()
        writer.writerows(filtered_content)
        