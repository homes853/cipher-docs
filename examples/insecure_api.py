import requests
import subprocess

def fetch_data(url):
    return requests.get(url, verify=False).json()

def run_cmd(user_input):
    subprocess.call("process " + user_input, shell=True)
