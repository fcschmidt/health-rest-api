"""
    Dictionaries for Test Data
"""

CLINICS_NOT_FOUND = {
    'clinic': {
        'id': 10
    },
    'physician': {
        'id': 1
    },
    'patient': {
        'id': 1
    },
    'text': 'Dipirona 1x ao dia'
}

CLINICS_INVALID_SYNTAX = {
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