class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = ["com", "bg", "net", "org"]

email = input()

while email != "End":

    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if email.count("@") <1:
        raise MustContainAtSymbolError("Email must contain @")
    if email.split(".")[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")

    email = input()

