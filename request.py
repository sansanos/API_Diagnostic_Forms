import requests
import configuration
import data

# Metodo POST para enviar formulario con datos validos
def post_create_form_valid():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_valid, verify=False)

# Metodo POST para enviar formulario con datos invalidos
def post_create_form_invalid():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_invalid, verify=False)

# Metodo POST para enviar formulario con 9 numeros en el campo Telefono 1
def post_create_form_9_numbers():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_9_numbers, verify=False)

# Metodo POST para enviar formulario con 11 numeros en el campo Telefono 1
def post_create_form_11_numbers():
    return requests.post(configuration.URL_FORM + configuration.POST_PATH, json=data.post_body_11_numbers, verify=False)