# Registrace uživatele
print("Registrace")
uzivatel_reg = input("Zadej jméno: ")
heslo_reg = input("Zadej heslo: ")

# Přihlášení uživatele
print("\nPřihlášení")
uzivatel_login = input("Zadej uživatele: ")
heslo_login = input("Zadej heslo: ")

# Kontrola jména a hesla
if uzivatel_reg != uzivatel_login:
    print("Špatné uživatelské jméno")
elif heslo_reg != heslo_login:
    print("Špatné heslo")
else:
    print("Přihlášení proběhlo v pořádku")

# Opakované přihlášení, dokud nezadá správné údaje
while uzivatel_reg != uzivatel_login or heslo_reg != heslo_login:
    print("Přihlášení")
    uzivatel_login = input("Zadej uživatele: ")
    heslo_login = input("Zadej heslo: ")

    if uzivatel_reg != uzivatel_login:
        print("Špatný uživatel")
    elif heslo_reg != heslo_login:
        print("Špatné heslo")
    else:
        print("Přihlášení proběhlo v pořádku")

# Kvíz o českém jazyce
print("\nOtestuj si znalosti z českého jazyka")

veta = "Pokud lidé píšou dotaz na úřad, měli by se snažit sepsat svůj dopis srozumitelně a jasně"

# Nahrazení znaků "_" za "i" nebo "y" na základě vstupu uživatele
nova_veta = veta.replace("i", "_").replace("y", "_")

# Zobrazení věty s nahrazenými znaky
print(nova_veta)

# Získání odpovědi od uživatele
odpoved = input("Doplňte znaky '_' za 'i' nebo 'y' a zadejte celou větu: ")

# Porovnání odpovědi uživatele s původní větou
if odpoved.lower() == veta.replace("_", "").lower():
    print("Správně!")
else:
    print(f"Nesprávně. Správná odpověď je: {veta}")
print("Kvíz dokončen.")