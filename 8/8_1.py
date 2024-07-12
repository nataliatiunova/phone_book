# отображение всех записей в телефонной книге
def show_contacts(filename):
    with open(filename, 'r') as file:  # with используется для автоматического закрытия файла после завершения работы с ним. r - режим чтения
        contacts = file.readlines()  # readlines() считывает все строки файла и сохраняет их в список contacts
        if not contacts:
            print("Телефонная книга пуста")
        else:
            for contact in contacts:
                parts = contact.strip().split(',')
                if len(parts) == 4: #пришлось добавить проверку строк на наличие 4 частей, чтобы не возникала ошибка при отображении
                    lastname, name, phone, notes = contact.strip().split(',')  # разделяет строку по запятой и убирает пробелы
                    print(f"Фамилия: {lastname}, Имя: {name}, Телефон: {phone}, Примечание: {notes}")

#добавление записи в телефонную книгу (привести к единому виду в дальнейшем)
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


'''# удаление контакта 
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
                print(f"Контакт {contact_lastname},{contact_name} удален.")'''

# обновление данных
# (Исправить:
# 1.нужно заново вводить все поля независимо от того, что нужно изменить
# 2. если в справочнике однофамильцы, то изменяются данные для обоих)
def update_contact(filename, lastname, name,  new_lastname, new_name, new_phone, new_notes):
    with open(filename, 'r') as file:
        contacts = file.readlines()
    with open(filename, 'w') as file:
        for contact in contacts:
            contact_lastname, contact_name, contact_phone, contact_notes = contact.strip().split(',')
            if (contact_name.lower() == name.lower() or
                contact_lastname.lower() == lastname.lower()):
                    file.write(f"{new_lastname}, {new_name},{new_phone},{new_notes} \n")
                    print(f"данные контакта {contact_lastname},{contact_name} обновлены")
            else:
                file.write(contact)

#сохранение в текстовом формате
def save_text(filename):
    with open(filename, 'r') as file:
        contacts = file.read()
    with open('phonebook.txt', 'w') as backup_file:
        backup_file.write(contacts)
    print("Справочник сохранен в текстовом формате как 'phonebook.txt'.")

#Копирование данных из одного файла в другой по номеру строки
def copy_line(filename, new_file, line_number):
        with open(filename, 'r') as file:
            lines = file.readlines()
            if line_number < 1 or line_number > len(lines):
                print(f"Неверный номер строки: {line_number}. Допустимые значения от 1 до {len(lines)}.")
                return

            line_to_copy = lines[line_number - 1].strip()

        with open(new_file, 'a'):
            new_file.write(line_to_copy + '\n')
        print(f"Строка {line_number} успешно скопирована в {new_file}.")

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента\n"
          "3. Изменить данные\n"
          "4. Добавить абонента в справочник\n"
          "5. Копирование данных из одного файла в другой по номеру строки\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    while True:
        try:
            choice = int(input("Введите номер действия: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до 7.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

#меню выбора действий
def main():
    filename = 'phone.txt'
    while True:
        choice = show_menu()

        if choice == 1: #отображение
            show_contacts(filename)
        elif choice == 2: #поиск
            isearch = input("Введите фамилию, имя, телефон или примечание для поиска: ")
            find_contact(filename, isearch)
        elif choice == 4: #добавление
            lastname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            notes = input("Введите заметки: ")
            add_contact(filename, lastname, name, phone, notes)
        elif choice == 3: #изменение
            lastname = input("Введите фамилию контакта для обновления: ")
            name = input("Введите имя контакта для обновления: ")
            new_lastname = input("Введите новую фамилию: ")
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый телефон: ")
            new_notes = input("Введите новые заметки: ")
            update_contact(filename, lastname, name, new_lastname, new_name, new_phone, new_notes)
        elif choice == 5:
            copy_line (filename, new_file, line_number)
            line_number = int(input("Введите номер строки для копирования: "))
            new_file = input("Введите имя файла для копирования: ")
        elif choice == 6:
            save_text(filename)
        elif choice == 7:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действительное действие.")

if __name__ == "__main__":
    main()

    