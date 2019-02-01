import re


def check_inc(fields):
    for field in fields:
        if not field:
            return "invalid"
    return "valid"


def check_user(fields):
    for field in fields:
        if not field or field.isspace():
            return "invalid"
    return "valid"


def check_email(mail):
    if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", mail):
        return "invalid"
    return "valid"


def check_paswd(passw):
    if len(passw) < 8:
        return "invalid"
    return "valid"
