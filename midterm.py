
pet_list = []
def add_pet(pet_name, pet_type, pet_status):
    new_pet = {
        "pet_name":pet_name,
        "pet_type":pet_type,
        "pet_status":pet_status
    }
 
    pet_list.append(new_pet)
    print("sucecess!")
def view_pets():
    pass
def display_menu():
    print("=== Pet Adoption Records ===")
    print("1. Add a pet")
    print("2. View all pets")
    print("3. Count available vs adopted")
    print("4. Find a pet by name")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    return choice

def main():
    running = True
    while running:
        
        choice = display_menu()
    
        match choice:
            case 1:
                name = input("Enter Pet Name: ")
                kind = input("Enter Pet Kind: ")
                status = input("Available [ 1 ] or Adopted [ 2 ]: ")
                add_pet(name, kind, status)
            case 2:
                for name,kind,status in new_pet:
                    print(f"Name: {name}\nAnimal Type: {kind}\nStatus: {status}")
            
    
        
main()