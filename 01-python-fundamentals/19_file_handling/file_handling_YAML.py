
# Use YAML FIles

import yaml
with open("./Practice_Files/config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("YAML Config:")
print(config)   
print("Database User from YAML file:", config['dev_db_config']['DB_USER'])
print("Database Password from YAML file:", config['dev_db_config']['DB_PASSWORD'])
print("Database Host from YAML file:", config['dev_db_config']['DB_HOST'])
print("Database Port from YAML file:", config['dev_db_config']['DB_PORT'])