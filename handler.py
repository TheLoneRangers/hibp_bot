import yaml
import app.hibp as hipb

def handler():
    with open(r'app/emails.yaml') as file:
        addy = yaml.full_load(file)

        for address in addy.items():
            hipb.check_address(address)
        
handler()