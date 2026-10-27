import re
def Asia(name):
    Asia_course=r"^[A-Z]{3}[0-9]{3}$"
    return bool(re.fullmatch(Asia_course, name))
print(Asia("TEC001"))
print(Asia("tec002"))