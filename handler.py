import yaml
import app.hibp

def handler():
    with open(r'/app/emails.yaml') as file:
        addy = yaml.full_load(file)

        for domain, address in addy.items():
            print(domain, ":", address)