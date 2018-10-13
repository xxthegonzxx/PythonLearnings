#!/usr/bin/env python3

import json
import argparse
import requests

# Get the data from config.json
with open('config.json') as read_file:
    data = json.load(read_file)

# Set variables we're going to use
headers = {'content-type': 'application/json'}
dev = data['dev']
demo = data['demo']
prod = data['prod']
commit = "My Commit Message"

if __name__ == '__main__':

    def helper():
        parser = argparse.ArgumentParser(description="Deploys application to dev/demo/prod environments", prog='app.py', usage='app.py -e <environment>')
        parser.add_argument("-e", required=True, help="The name of the environment to deploy to. Choices are dev/demo/prod")
        args = parser.parse_args()
        env = args.e
        if env == "dev":
            print("deploying to dev {}".format(dev), commit)
        elif env == "demo":
            print("deploying to demo {}".format(demo), commit)
        elif env == "prod":
            print("deploying to prod {}".format(prod), commit)


    # req = requests.get(prod, headers=headers) # This will fail since it's a fake API endpoint but you get the idea...

helper()
