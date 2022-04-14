import requests
import yaml


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
        _res = requests.get(f"https://xyzcompany.com/{self.last.replace(' ', '')}/{month}")
        if _res.ok:
            return _res.text
        else:
            raise BadResponseException


class EtlBaseClass:

    def __init__(self, job_name: str, env: str = 'test'):
        self.job_name = job_name

        # using setter for assignment

        self.env = env

    # getter
    @property
    def env(self):
        return self._env

    # setter
    @env.setter
    def env(self, env):
        # Some sample validation
        _valid_ens = ['prod', 'dev', 'uat', 'test']
        if env in _valid_ens:
            self._env = env
        else:
            raise Exception(f"Invalid environment argument passed. Please choose from :{_valid_ens}")


class EtlColumnConfigBaseClass:
    def __init__(self, config_file_path: str = None):
        # Instantiation will run and create the attributes dynamically if
        # config file is passed as an argument

        if config_file_path:
            self._conf_path = config_file_path
            self._load_file_attributes()
        # other required attributes#

    # Private instance method for loading attributes from config file
    def _load_file_attributes(self):
        with open(self._conf_path) as yml_conf:
            conf = yaml.safe_load(yml_conf)
        for col in conf['data']['columns']:
            self.__setattr__(col, conf['data']['columns'][col])

    # overriding __getattr__ for handling case insensitivity scenario
    def __getattr__(self, item):
        return self.__getattribute__(item.lower())
