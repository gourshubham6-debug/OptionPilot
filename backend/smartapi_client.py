from SmartApi import SmartConnect
from dotenv import load_dotenv
import os
import pyotp

load_dotenv()

API_KEY = os.getenv("API_KEY")
CLIENT_CODE = os.getenv("CLIENT_CODE")
MPIN = os.getenv("MPIN")
TOTP_SECRET = os.getenv("TOTP_SECRET")


def login():
    obj = SmartConnect(api_key=API_KEY)

    totp = pyotp.TOTP(TOTP_SECRET).now()

    session = obj.generateSession(
        CLIENT_CODE,
        MPIN,
        totp
    )

    return obj, session


def get_index_quotes():
    obj, session = login()

    nifty = obj.ltpData(
        "NSE",
        "NIFTY 50",
        "99926000"
    )

    sensex = obj.ltpData(
        "BSE",
        "SENSEX",
        "99919000"
    )

    return {
        "nifty": nifty.get("data"),
        "sensex": sensex.get("data")
    }
