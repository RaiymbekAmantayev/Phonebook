import json

class PhoneBookBase():
    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

class PhoneBook():
    def __init__(self, file):
        self.file = file
        self.date_list = []
        self.load_dates()

    def load_dates(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for get_data in data:
                    date = PhoneBookBase(**get_data)
                    self.date_list.append(date)
        except FileNotFoundError:
            pass
    
    def save_dates(self):
        data = [{
            'last_name': date.last_name,
                 'first_name': date.first_name,
                 'middle_name': date.middle_name,
                 'organization': date.organization,
                 'work_phone': date.work_phone,
                 'personal_phone': date.personal_phone}
                 for date in self.date_list]
        with open(self.file, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_data(self, data):
        self.date_list.append(data)
        self.save_dates()

    def update(self, index, data):
        if 0 < index <=len(self.date_list):
            self.date_list[index] = data
            self.save_dates()

    def delete(self, index):
        if 0 < index <=len(self.date_list):
            del self.date_list[index]
            self.save_dates()
            print("Запись удалена.")
        else:
            print("Некорректный номер записи.")
            
    def search_data(self, search_data):
        results = []
        for data in self.date_list:
            if (search_data.lower() in data.last_name.lower()) or (search_data.lower() in data.first_name.lower()):
                results.append(data)
        return results


    def display_entries(self, page, count_of_date):
        start_idx = (page - 1) * count_of_date
        end_idx = start_idx + count_of_date
        for idx, data in enumerate(self.date_list[start_idx:end_idx], start=start_idx + 1):
            print(f"{idx}. {data.last_name} { data.first_name} { data.middle_name}")
            print(f"   Организация: {data.organization}")
            print(f"   Рабочий телефон: {data.work_phone}")
            print(f"   Личный телефон: {data.personal_phone}")
            print("=" * 40)
def main():
    phonebook = PhoneBook('phonebook.json')

    while True:
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Удаление записи")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            page = int(input("Введите номер страницы: "))
            count_of_date = 5
            phonebook.display_entries(page, count_of_date)
        
        elif choice == "2":
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            middle_name = input("Отчество: ")
            organization = input("Организация: ")
            work_phone = input("Рабочий телефон: ")
            personal_phone = input("Личный телефон: ")
            data = PhoneBookBase(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            phonebook.add_data(data)
        elif choice == "3":
            index = int(input("Введите номер записи для редактирования: ")) - 1
            if 0 <= index < len(phonebook.date_list):
                data = phonebook.date_list[index]
                last_name = input("Новая фамилия: ")
                first_name = input("Новое имя: ")
                middle_name = input("Новое отчество: ")
                organization = input("Новая организация: ")
                work_phone = input("Новый рабочий телефон: ")
                personal_phone = input("Новый личный телефон: ")
                new_data = PhoneBookBase(last_name, first_name, middle_name, organization, work_phone, personal_phone)
                phonebook.update(index, new_data)
            else:
                print("Некорректный номер записи")
        
        elif choice == "4":
            search_data = input("Введите строку для поиска: ")
            results = phonebook.search_data(search_data)
            if results:
                for idx, entry in enumerate(results, start=1):
                    print(f"{idx}. {entry.last_name} {entry.first_name} {entry.middle_name}")
                    print(f"   Организация: {entry.organization}")
                    print(f"   Рабочий телефон: {entry.work_phone}")
                    print(f"   Личный телефон: {entry.personal_phone}")
                    print("=" * 40)
            else:
                print("Записи не найдены")
        elif choice == "5":
            index_of_date = int(input("Выберите запись для удаление: "))
            phonebook.delete(index_of_date)
        elif choice == "0":
            break
        else:
            print("Некорректный выбор")

if __name__ == "__main__":
    main()
