# Функция для отображения всех записей в телефонной книге
def show_contacts(filename):
    with open(filename, 'r') as file: # with используется для автоматического закрытия файла после завершения работы с ним. r - режим чтения
        contacts = file.readlines() #readlines() считывает все строки файла и сохраняет их в список contacts
        if not contacts:
            print("Телефонная книга пуста")
        else:
            for contact in contacts:
                lastname, name, phone, notes = contact.strip().split(',') #разделяет строку по запятой и убирает пробелы
                print(f"Фамилия: {lastname}, Имя: {name}, Телефон: {phone}, Примечание: {notes}")

#добавление записи в телефонную книгу
def add_contact(filename, lastname, name, phone, notes):
    with open(filename, 'a') as file: #oткрывает файл с именем filename в режиме добавления ('a') и закрывает после работы с ним
        #добавление происходит в конец файла (как append)
        file.write(f"{lastname},{name},{phone},{notes}\n")

# поиск по всем параметрам
def find_contact(filename, isearch):
    found = False
    with open(filename, 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            lastname, name, phone, notes = contact.strip().split(',')
            if (isearch.lower() in lastname.lower() or 
            isearch.lower() in name.lower() or
            isearch.lower() in phone.lower() or
            isearch.lower() in notes.lower()):
                found = True
                print(f"Фамилия: {lastname}, Имя: {name}, Телефон: {phone}, Примечание: {notes}")
                return
        if not found:
            print("Контакт не найден")


# удаление контакта 
def delete_contact(filename, lastname, name, phone, notes):
    with open(filename, 'r') as file:
        contacts = file.readlines()
    with open(filename, 'w') as file: #'w' - Режим записи.
            for contact in contacts:
                contact_lastname, contact_name, contact_phone, contact_notes = contact.strip().split(',')
            if (contact_lastname.lower() != lastname.lower() or
            contact_name.lower() != name.lower or
            contact_phone.lower() != phone.lower() or
            contact_notes.lower() != notes.lower()):
                file.write(contact+ '\n')
            else:
                print(f"Контакт {contact_lastname},{contact_name} удален.")

# обновление телефона 
def update_contact(filename, lastname, name, new_phone):
    with open(filename, 'r') as file:
        contacts = file.readlines()
    with open(filename, 'w') as file:
        for contact in contacts:
            contact_lastname, contact_name, contact_phone = contact.strip().split(',')
            if (contact_name.lower() == name.lower() or
                contact)contact_lastname == lastname.lower()):
                    file.write(f"{contact_lastname}, {contact_name},{new_phone}\n")
                    print(f"Телефон контакта {contact_lastname},{contact_name} обновлен")
            else:
                file.write(contact)

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice