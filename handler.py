import yaml
import app.hibp as hipb

def handler():
    with open(r'app/emails.yaml') as file:
        addys = yaml.safe_load(file)

        for address in addys:
            hipb.check_address(address)
        
handler()