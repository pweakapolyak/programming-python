import configparser

import requests
import urllib3


class ApiConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./gk/gk.ini')

    @property
    def url(self):
        return self.config['API']['url']

    @property
    def course_name(self):
        return self.config['API']['course_name']


class ApiKeyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ApiKeyIncorrect(Exception):
    def __init__(self, message):
        super().__init__(message)


class AssignmentNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class AssignmentNotAllow(Exception):
    def __init__(self, message):
        super().__init__(message)


class GkAssignmentRequest:
    def __init__(self, step: int, num: int, answers: dict):
        self.step = step
        self.num = num
        self.answers = answers

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value

    def json(self):
        with open('./gk/key.txt', 'r') as file:
            api_key = file.read().rstrip()
        if api_key is None:
            raise ApiKeyError('GK_API_KEY not set in environment variable')

        return {
            "key": api_key.strip(),
            "num": self.num,
            "answers": self.answers
        }


class GkApi:
    def __init__(self):
        self.config = ApiConfig()

    def do_assignments(self, request: GkAssignmentRequest):
        json = request.json()
        urllib3.disable_warnings()
        response = requests.post(self.__construct_url__(request.step), json=json, verify=False)

        if response.status_code == 401:
            raise ApiKeyIncorrect(f'GK_API_KEY<%s> is incorrect' % json['key.txt'])
        if response.status_code == 404:
            raise AssignmentNotFound(f'Assignment<%s> not found' % request.step)
        if response.status_code == 400:
            raise AssignmentNotAllow(f'Assignment<%s> not allow for you' % request.step)

        return response.json()

    def __construct_url__(self, step):
        return self.config.url + "/assignment/" + self.config.course_name + "/" + str(step) + "/submit"


if __name__ == '__main__':
    import os
    os.chdir('../..')
    gk_api = GkApi()
    req = GkAssignmentRequest(5, 1, {"a": "b", "b": "a"})
    try:
        resp = gk_api.do_assignments(req)
    except Exception as error:
        print(error)
