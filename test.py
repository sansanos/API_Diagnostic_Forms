import request

def possitive_assert(response):
    code = response.status_code
    assert code == 200

def test_post_valid():
    response = request.post_create_form_valid()
    possitive_assert(response)

def test_post_9_numbers():
    response = request.post_create_form_9_numbers()
    possitive_assert(response)

def negative_assert(response):
    code = response.status_code
    assert code == 422

def test_post_invalid():
    response = request.post_create_form_invalid()
    negative_assert(response)

def test_post_11_numbers():
    response = request.post_create_form_11_numbers()
    negative_assert(response)