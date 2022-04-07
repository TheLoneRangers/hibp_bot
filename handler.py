import yaml
import app.hibp as hipb

def handler(payload, context):
    if payload["auto"] = true:
        return hibp.auto_check
    else:
        return hibp.parameterized_check(payload)
        
handler(payload, context)
