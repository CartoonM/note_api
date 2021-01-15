from email_validator import validate_email, EmailNotValidError

from .errors import InvalidEmail


def check_email(email: str) -> str:
    try:
        valid = validate_email(email,
                               allow_smtputf8=False,
                               check_deliverability=False)
        return valid.email
    except EmailNotValidError as err:
        raise InvalidEmail(str(err))
