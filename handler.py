import yaml
import app.hibp as hipb

def handler():
    with open(r'app/emails.yaml') as file:
        addy = yaml.full_load(file)

        for domain, address in addy.items():
            # print(domain, ":", address)
            hipb.check_address(domain, address)
        
handler()