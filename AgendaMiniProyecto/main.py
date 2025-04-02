# Definir función para el loop principal
def main():
    contact_list = [] # Definir lista/array de contactos
    while True:
        print("\nAGENDA DE CONTACTOS")
        
        print("\n1- Agregar contacto")
        print("2- Busca un contacto")
        print("3- Eliminar contacto")
        print("4- Ver todos los contactos")
        print("5- Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            # Agrega un contacto
            print("\nAgrega un contacto")
            addContact(contact_list)
        elif option == "2":
            # Busca un contacto
            print("\nBusca un contacto")
            searchContact(contact_list)
        elif option == "3":
            # Elimina un contacto
            print("\nElimina un contacto")
            removeContact(contact_list)
        elif option == "4":
            # Ver todos los contactos
            print("\nVer todos los contactos")
            seeAllContacts(contact_list)
        elif option == "5":
            # Salir
            print("\nSalir")
            break
        else:
            print("\nOpción no válida")

def addContact(contact_list):
    name = input("\nIngresa un nombre: ").strip()
    phone = input("Ingrea un número de celular: ").strip()
    email = input("Ingresa un correo electronico: ").strip()

    for contact in contact_list:
        if contact["name"] == name:
            print("\nEl nombre del contacto esta en uso!")
            return
            
    contact_list.append({"name": name, "phone": phone, "email": email})
    print(f"\nContacto {name} agregado")

def removeContact(contact_list):
    name = input("\nIngresa un nombre: ").strip()
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print(f"\nContacto {name} eliminado")
            return
    
    print(f"\nContacto no encontrado")

def searchContact(contact_list):
    name = input("\nIngresa un nombre: ").strip()
    search = []
    for contact in contact_list:
        if contact["name"].startswith(name): 
            search.append(contact)

    if not search:
        print("No hay resultados")
    else:
        for contact in search:
            print(f"{contact['name']}: {contact['phone']} - {contact['email']}")        

def seeAllContacts(contact_list):
    if not contact_list:
        print("\nLa agenda está vacía")
    else:
        for contact in contact_list:
            print(f"{contact['name']}: {contact['phone']} - {contact['email']}")

if __name__ == "__main__":
    main()
