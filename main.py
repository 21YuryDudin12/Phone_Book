
phone_book = {}
PATH = "phones.txt"


def open_file(book: dict):
    with open(PATH, "r+", encoding = 'UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data,1):
        contact = contact.strip().split(';')
        book[i] = contact

def save_file(book: dict):
    all_contact = []
    for contact in book.values():
        all_contact.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF=8') as file:
        file.write('\n'.join(all_contact))
    
def show_contacts(book: dict, message: str):
    print('\n' + '='*67 )
    if book:
        for i, contact in book.items():
            print(f'{i}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print('Phone book is empty')
    print('='*67 + '\n')

def add_new_contact(book: list, new: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new

def find_contact(book: dict, search: str):
    result = {}
    for i, contact in book.items():
        for field in contact:
            if search in field.lower():
                result[i] = contact
                break
    return(result)

def func_search(book: dict):
    search = input('What do u want to search?')
    result = find_contact(book, search)
    show_contacts(result, f'The contact witch you want to search is not found!')

def change_contact(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    ch = []
    for item in ['Write new name(or pass): ','Write new phone(or pass): ','Write new comment(or pass): ']:
        ch.append(input(item))
    book[cid] = [ch[0] if ch[0] else name, ch[1] if ch[1] else phone, ch[2] if ch[2] else comment, ]
    return ch[0] if ch[0] else name

def delete_contact(book: dict, cid: int):
    name = book.pop(cid)
    return name[0]


def menu():
    menu_points = ['Open file', 
                   'Save file',
                   'See all contacts',
                   'Add contact',
                   'Find contact',
                   'Change contact',
                   'Delete contact',
                   'Exit',
                   'Save and exit']
    print('Main menu')
    [print(f'\t{i}.{item}') for i, item in enumerate(menu_points, 1)]
    choice = int(input('Take the point of menu: '))
    return choice

while True:
    choice = menu()
    match choice:
        case 1:
            open_file(phone_book)
            print('\nPhone book sucsessfuly opened!\n ')
        case 2:
             save_file(phone_book)
             print('\nPhone book sucsessfuly saved!\n ')
        case 3:
            show_contacts(phone_book, 'Phone book is empty')
        case 4:
            new = []
            for item in ['Write name: ','Write phone: ','Write comment: ']:
                new.append(input(item))
            add_new_contact(phone_book, new)
            print(f'\nContact{new[0]} sucsessfuly added\n')
        case 5:
            func_search(phone_book)
        case 6:
            func_search(phone_book)
            select = int(input('Wich contact do u need to change?'))
            name = change_contact(phone_book,select)
            print(f'\nContact {name} sucsessfuly changed!\n')
        case 7:
            func_search(phone_book)
            select = int(input('Wich contact do u need to delete?'))
            name = delete_contact(phone_book,select)
            print(f'\nContact {name} sucsessfuly deleted!\n')
        case 8:
            print('\nGoodbye!')
            break
        case 9:
            save_file(phone_book)
            print('\nChanges are saved. Goodbye!')
            break
