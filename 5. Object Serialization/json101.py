import json

'''
    loading json from file
'''
with open('test.json') as file:
    json_data = json.load(file)

print(json_data)


'''
    saving json
'''
new_json = '{"title": "Sample Konfabulator Widget","name": "main_window","color": "green"}'

with open('test.json', 'w') as file:
    json.dump(new_json, file)


