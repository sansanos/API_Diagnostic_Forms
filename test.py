import request

# Funcion para validar codigo de respuesta exitosa
def possitive_assert(response):
    code = response.status_code
    assert code == 200

# 1 Validacion formulario con datos validos
def test_post_valid():
    response = request.post_create_form_valid()
    possitive_assert(response)

# 2 Validacion campo Telefono 1 con 9 numeros
def test_post_9_numbers():
    response = request.post_create_form_9_numbers()
    possitive_assert(response)

# Funcion para validar codigo de respuesta fallida
def negative_assert(response):
    code = response.status_code
    assert code == 422

# 4 Validacion formulario con datos invalidos
def test_post_invalid():
    response = request.post_create_form_invalid()
    negative_assert(response)

# 5 Validacion campo Telefono 1 con 11 numeros
def test_post_11_numbers():
    response = request.post_create_form_11_numbers()
    negative_assert(response)