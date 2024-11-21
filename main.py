from services.manager import LibraryManager

def main():
    manager = LibraryManager(data_file="data/library.json")
    while True:
        print("\n1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Поиск книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            manager.show_all_books()
        elif choice == "2":
            manager.add_book()
        elif choice == "3":
            manager.remove_book()
        elif choice == "4":
            manager.search_books()
        elif choice == "5":
            manager.change_status()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
