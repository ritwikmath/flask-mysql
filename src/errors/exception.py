from flask import Response
import json

def handleException(e):
    print(e)
    resp = Response(json.dumps({"error":"Something went wrong"}), 500)  
    return resp