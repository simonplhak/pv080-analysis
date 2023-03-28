import urllib3 as urllib

import flask
import yaml
from debugpy._vendored.pydevd.pydev_sitecustomize.sitecustomize import raw_input

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    try:
        http = urllib.PoolManager()
        r = http.request("GET", url)
    except:
        print("Exception")


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.safe_load(stream)  # deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if password != "Iloveyou":
        raise Exception('Invalid password')
    print("Successfully authenticated!")


if __name__ == "__main__":
    print("Vulnerabilities:")
    print(
        "1. Format string vulnerability: use string={person.__init__.__globals__[CONFIG][API_KEY]}"
    )
    print("2. Code injection vulnerability: use string=;print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: run program with -O argument")
    choice = raw_input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(raw_input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = raw_input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(raw_input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = raw_input("Enter master password: ")
        authenticate(password)
