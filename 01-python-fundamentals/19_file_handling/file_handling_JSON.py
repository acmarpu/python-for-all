# Use JSON FIles
import json
with open("./Practice_Files/config.json", "r") as file:
    config = json.load(file)

print("JSON Config:")
print(config)
print("Database User from JSON file:", config['dev_db_config']['username'])
print("Database Password from JSON file:", config['dev_db_config']['password'])
print("Database Host from JSON file:", config['dev_db_config']['host'])
print("Database Port from JSON file:", config['dev_db_config']['port'])