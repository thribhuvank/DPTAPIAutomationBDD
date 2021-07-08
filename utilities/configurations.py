import configparser

import jsonpath
import requests

from utilities.resources import FranApiResources


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getFranAccessToken():
    url = getConfig()['API']['baseurl'] + FranApiResources.login
    body = {'username': '9880308886', 'password': 'shop@2021'}
    franlogin = requests.post(url, data=body)
    fran_token = jsonpath.jsonpath(franlogin.json(), 'data.access_token')
    FRAN_ACCESSTOKEN = 'Bearer ' + fran_token[0]
    return FRAN_ACCESSTOKEN


def getAccAccessToken():
    url = getConfig()['API']['baseurl'] + FranApiResources.login
    body = {'username': '9066343126', 'password': 'shop@2021'}
    acclogin = requests.post(url, data=body)
    acc_token = jsonpath.jsonpath(acclogin.json(), 'data.access_token')
    ACC_ACCESSTOKEN = 'Bearer ' + acc_token[0]
    return ACC_ACCESSTOKEN


def getBillAccessToken():
    url = getConfig()['API']['baseurl'] + FranApiResources.login
    body = {'username': '9898989898', 'password': 'Rohit@5678'}
    billlogin = requests.post(url, data=body)
    bill_token = jsonpath.jsonpath(billlogin.json(), 'data.access_token')
    BILL_ACCESSTOKEN = 'Bearer ' + bill_token[0]
    return BILL_ACCESSTOKEN


def getBillExAccessToken():
    url = getConfig()['API']['baseurl'] + FranApiResources.login
    body = {'username': '8105425516', 'password': 'shop@2021'}
    billexlogin = requests.post(url, data=body)
    billex_token = jsonpath.jsonpath(billexlogin.json(), 'data.access_token')
    BIEX_ACCESSTOKEN = 'Bearer ' + billex_token[0]
    return BIEX_ACCESSTOKEN