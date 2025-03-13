def check_lenght(stringa):
    if len(stringa) > 10:
        print(f"{stringa} ha più di 10 caratteri")
    elif len(stringa) < 10:
        print(f"{stringa} ha meno di 10 caratteri")
    else:
        print(f"{stringa} ha 10 caratteri")
check_lenght(input(f"insersisci la stringa: "))
