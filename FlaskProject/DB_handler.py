import pyrebase
import json


class DBModule:
    def __init__(self):
        with open("./auth/firebase_auth.json") as f:
            config = json.load(f)
        self.firebase = pyrebase.initialize_app(config)

    def login(self, id, pw):
        pass

    def sing_in(self, id, pw, name, email):
        pass

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
