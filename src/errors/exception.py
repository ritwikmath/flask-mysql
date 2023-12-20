from flask import jsonify
import traceback
import os
import sys

def handleException(e):
    data = {"error":"Something went wrong"}
    if os.getenv("ENV") == "DEV":
        data.update({
            "traceback": traceback.format_exc()
        })
    return jsonify(data), 500