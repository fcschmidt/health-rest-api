"""
    Dictionaries for Test Data
"""

PATIENTS_NOT_FOUND = {
    'clinic': {
        'id': 1
    },
    'physician': {
        'id': 1
    },
    'patient': {
        'id': 10
    },
    'text': 'Dipirona 1x ao dia'
}

PATIENTS_INVALID_SYNTAX = {
    'clinic': {
        'id': 1
    },
    'physician': {
        'id': 1
    },
    'patient': {
        'id': 'dasdwqdqw'
    },
    'text': 'Dipirona 1x ao dia'
}
