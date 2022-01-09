import requests


class BadResponseException(Exception):
    def __init__(self):
        _message = "Bad Response!!"
        super().__init__(_message)


class Employee:
    def __init__(self, name):
        self.full_name = name

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.replace(' ', '').lower()}@xyzcompany.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first = name.strip().split(" ")[0]
        self.last = " ".join(name.strip().split(" ")[1:])

    def get_monthly_target(self, month):
        _res = requests.get(f"https://xyzcompany.com/{self.last.replace(' ','')}/{month}")
        if _res.ok:
            return _res.text
        else:
            raise BadResponseException
