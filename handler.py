import yaml
from app.hibp import auto_check, check_address 

#test payloads
##auto 
#payload = {"auto":"true"}
##not auto
payload={"address":"jhargr200@gmail.com", "auto":"false"}

context = {} 

def handler(payload, context):
    if payload["auto"] == "true":
        auto_check()
    else:
        check_address(payload["address"])
        
handler(payload, context)
