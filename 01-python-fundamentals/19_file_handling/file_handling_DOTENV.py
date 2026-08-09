#  Use config files
# Types of config files: use .env files 
'''''
due to security reasons, we should not store sensitive information in the code. 
Instead, we can use environment variables to store sensitive information such as API keys, 
database credentials, etc. 
We can use the python-dotenv package to load environment variables from a .env file.
''''' 
# Create a .env file in the root directory of your project and add the following lines to it:
# API_KEY=your_api_key_here
# GITHUB_TOKEN=your_github_token_here

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")

git_token = os.getenv("GITHUB_TOKEN")
print(f"GitHub Token: {git_token}")


# Using configparser ini files
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

env= 'dev'
print("Section:', config.sections())")
print("database User:", config[env + '_db_config']['DB_USER'])
print("database Password:", config[env + '_db_config']['DB_PASSWORD'])
print("database Host:", config[env + '_db_config']['DB_HOST'])
print("database Port:", config[env + '_db_config']['DB_PORT'])