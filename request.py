import requests
import configuration
import data

def post_create_form_valid():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_valid, verify=False)

def post_create_form_invalid():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_invalid, verify=False)

def post_create_form_9_numbers():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_9_numbers, verify=False)

def post_create_form_11_numbers():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_11_numbers, verify=False)