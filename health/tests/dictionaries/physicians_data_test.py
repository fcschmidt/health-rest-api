"""
    Dictionaries for Test Data
"""

PHYSICIANS_NOT_FOUND = {
    'clinic': {
        'id': 1
    },
    'physician': {
        'id': 10
    },
    'patient': {
        'id': 1
    },
    'text': 'Dipirona 1x ao dia'
}

PHYSICIANS_INVALID_SYNTAX = {
    'clinic': {
        'id': 1
    },
    'physician': {
        'id': 'string'
    },
    'patient': {
        'id': 1
    },
    'text': 'Dipirona 1x ao dia'
}
