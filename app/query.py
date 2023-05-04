import requests


def getIp():

    url = "https://ifconfig.me/ip"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def getTime(ip):
    url = f"https://www.timeapi.io/api/Time/current/ip?ipAddress={ip}"

    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
