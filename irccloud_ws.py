
import sys

from twisted.internet import reactor
from twisted.python import log
from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS
import requests
import traceback
import logging
import json
import time
from timeloop import Timeloop
from websockets import connect
import ssl
from datetime import timedelta
import random
from os import environ, urandom
from base64 import encodebytes as base64encode
import asyncio
import logging



class irccloud:
    """
    This is a very simple class that takes an user's irc user name
    and password as input and keeps the connection alive to emulate
    the hearbeat produced due to real browser activity.
    """
    AuthenticationToken = ""
    SessionId = ""
    KeepAliveToken = ""

    def __init__(self, email, password):
        self.email = email
        self.password = password
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)
        self.log = logging.getLogger(__name__)

    def get_authentication_token(self):
        url = "https://www.irccloud.com/chat/auth-formtoken"
        r = requests.post(url)
        response = r.json()
        if response["success"]:
            self.log.info("Successfully obtained authentication token.")
            irccloud.AuthenticationToken = response["token"]
        else:
            self.log.error("Failed to obtain an authentication token.")
            irccloud.AuthenticationToken = "AUTH_FAILURE"

    def get_session_id(self):
        self.get_authentication_token()
        if irccloud.AuthenticationToken == "AUTH_FAILURE":
            return irccloud.AuthenticationToken
        else:
            login_url = "https://www.irccloud.com/chat/login"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "x-auth-formtoken":irccloud.AuthenticationToken
            }
            login_data = {
                "email" : self.email,
                "password" : self.password,
                "token" : irccloud.AuthenticationToken
            }
            r = requests.post(login_url, data = login_data, headers = headers)
            response = r.json()
            if response["success"]:
                self.log.info("Successfully obtained a session id.")
                irccloud.SessionId = response["session"]
            else:
                self.log.critical("Failed to obtain a session id.")
                irccloud.SessionId = "SESSION_FAILURE"

    def get_secure_key(self):
        randomness = urandom(16)
        return base64encode(randomness).decode('utf-8').strip()

    def ws_keep_alive(self):
        ssl_context = ssl.SSLContext()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        ua_file = open("user_agents.json", "r+")
        user_agents = json.load(ua_file)
        ua_file.close()
        ws_url = "wss://api.irccloud.com/"
        ws_origin = "https://api.irccloud.com"
        irc_cloud_header = {
            "Connection": "Upgrade",
            "Host": "api.irccloud.com",
            "Origin": ws_origin,
            "User-Agent": random.choice(user_agents),
            "Cookie": "session={0}".format(irccloud.SessionId),
            "Sec-WebSocket-Key": self.get_secure_key(),
            "Sec-WebSocket-Version": "13",
            "Upgrade": "WebSocket"
        }
        factory = WebSocketClientFactory(ws_url, headers=irc_cloud_header)
        connectWS(factory)
        reactor.run()

    def runner(self):
        self.get_session_id()
        self.log.debug("   IRC Cloud Keep alive Func   ")
        if irccloud.SessionId == "SESSION_FAILURE":
            self.log.critical("Couldn't get a session initialized. Quitting... :(")
            sys.exit(0)
        else:
            self.ws_keep_alive()
            if irccloud.KeepAliveToken == "KA_ALIVE":
                self.log.info("IRC Cloud Session is Kept alive.")
            else:
                self.log.error("IRC Cloud Session could not be Kept alive.")

def timed_executor():
    try:
        email = environ.get("IRCCLOUD_USERNAME")
        password = environ.get("IRCCLOUD_PASSWORD")
        irc = irccloud(email, password)
        irc.runner()
    except KeyboardInterrupt:
        irc.log.debug("Shutdown requested. Exiting script. Thank you :)")
        sys.exit(0)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    timed_executor()
