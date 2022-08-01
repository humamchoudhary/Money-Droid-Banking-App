class InvalidCardError(Exception):
    """Invalid Card Number"""
    pass


class InsufficientBalanceError(Exception):
    """Insufficient Balance"""
    pass


class InvalidCVVError(Exception):
    """Invalid CVV"""
    pass


class InvalidAccountNumberError(Exception):
    """Invalid Account Number"""
    pass


class AccountExistsError(Exception):
    """Dublicate account"""
    pass


class AccountNotFoundError(Exception):
    """Invalid UserName"""
    pass


class InvalidPasswordError(Exception):
    """Password does not match"""
    pass


class InvalidAmount(Exception):
    """Invalid amount"""
    pass

class InvalidEmailError(Exception):
    """Invalid Email"""
    pass

class InvalidRefNumber(Exception):
    """Invalid Ref Number of the bill"""
    pass
