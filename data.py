post_body_valid = {
  "test_type": [
    "Prueba 1"
  ],
  "city": "Medellín",
  "doctor": "Orlando",
  "country": "Colombia",
  "institution": "Institución 2",
  "pathology": "LINFOMA HODGKIN CLÁSICO CON PROGRESIÓN A TAMO Y  BRENTUXIMAB VEDOTINA",
  "patient_id": "1",
  "patient_name": "Jorge",
  "patient_lastname": "Toro Agudelo",
  "prefix1": "+57",
  "telephone1": "3131234567",
  "prefix2": "",
  "telephone2": "",
  "address": "Calle 33sur #32 - 29",
  "consent": True
}

post_body_invalid = {
  "test_type": [
    "Prueba 1"
  ],
  "city": "",
  "doctor": "",
  "country": "",
  "institution": "",
  "pathology": "",
  "patient_id": "",
  "patient_name": "",
  "patient_lastname": "",
  "prefix1": "",
  "telephone1": "",
  "prefix2": "",
  "telephone2": "",
  "address": "",
  "consent": None
}

post_body_9_numbers = {
  "test_type": [
    "Prueba 1"
  ],
  "city": "Medellín",
  "doctor": "Orlando",
  "country": "Colombia",
  "institution": "Institución 2",
  "pathology": "LINFOMA HODGKIN CLÁSICO CON PROGRESIÓN A TAMO Y  BRENTUXIMAB VEDOTINA",
  "patient_id": "1",
  "patient_name": "Jorge",
  "patient_lastname": "Toro Agudelo",
  "prefix1": "+57",
  "telephone1": "313123456",
  "prefix2": "",
  "telephone2": "",
  "address": "Calle 33sur #32 - 29",
  "consent": True
}

post_body_11_numbers = {
  "test_type": [
    "Prueba 1"
  ],
  "city": "Medellín",
  "doctor": "Orlando",
  "country": "Colombia",
  "institution": "Institución 2",
  "pathology": "LINFOMA HODGKIN CLÁSICO CON PROGRESIÓN A TAMO Y  BRENTUXIMAB VEDOTINA",
  "patient_id": "1",
  "patient_name": "Jorge",
  "patient_lastname": "Toro Agudelo",
  "prefix1": "+57",
  "telephone1": "31312345678",
  "prefix2": "",
  "telephone2": "",
  "address": "Calle 33sur #32 - 29",
  "consent": True
}