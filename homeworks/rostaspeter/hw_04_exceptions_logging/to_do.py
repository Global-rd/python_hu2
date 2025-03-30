import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[logging.StreamHandler(), logging.FileHandler("app.log")])

commands = ["1", "2", "3", "4"]

def add(input):
    if input:
        try:
            with open("empty.txt", 'a') as file:
                file.write(f"{input}\n")
                file.close()
        except Exception as error:
            logging.error(f"Hiba: {error}")
    else:
        logging.warning(f"Nem tudsz üres mezőt hozzáadni")

def view():
    with open("empty.txt", 'r') as file:
        content = file.readlines()
        file.close()
    if content == []:
        return print("\nNincs egy elem se!")
    for number, line in enumerate(content, 0):
        print(f"\n{number}: {line.strip()}")

def remove(input):
    with open("empty.txt", 'r') as file:
        content = file.readlines()
        file.close()
    if content == []:
        return print("\nNincs egy elem se!")
    for number, line in enumerate(content, 0):
        if int(input) == int(number):
            content.pop(number)
        file.close()
    with open("empty.txt", 'w') as file:
        file.writelines(content)
        file.close()

def choices():
    print("\n1: Add Task:")
    print("2: View Task:")
    print("3: Remove Task:")
    print("4: Exit\n")

while True:
    choices()
    choice = str(input("Válassz egy parancsot!: "))
    if choice in commands:
        if choice == "1":
            user_input = input("\nÍrd le amit hozzá szeretnél adni!: ")
            add(user_input)
        elif choice == "2":
            view()
        elif choice == "3":
            view()
            user_input = input("\nAdd meg a számát, melyet ki szeretnél törölni: ")
            try:
                remove(user_input)
            except Exception as error:
                print(f"Hiba: {error}")
        elif choice == "4":
            print("Bezárás...")
            exit()
    else:
        print("\nHelytelen válasz!")