# error_tracker.py

error_log = []

def track_error(location, message):
    error_log.append({
        'location': location,
        'error': message
    })

def get_errors():
    return error_log
