import json
import os
from typing import List, Dict, Union

# Путь к файлу, в котором будут храниться данные
FILENAME = 'library.json'


def load_books() -> List[Dict[str, Union[int, str]]]:
    """Загружает книги из файла."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def save_books(books: List[Dict[str, Union[int, str]]]) -> None:
    """Сохраняет книги в файл."""
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(title: str, author: str, year: str) -> None:
    """Добавляет книгу в библиотеку."""
    books = load_books()
    book_id = max([book['id'] for book in books], default=0) + 1
    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' добавлена с id {book_id}.")


def delete_book(book_id: int) -> None:
    """Удаляет книгу из библиотеки."""
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            save_books(books)
            print(f"Книга с id {book_id} удалена.")
            return
    print(f"Книга с id {book_id} не найдена.")


def search_books(query: str, field: str) -> None:
    """Ищет книги по заданному полю."""
    books = load_books()
    results = [book for book in books if query.lower() in book[field].lower()]
    if results:
        for book in results:
            print(book)
    else:
        print(f"Книги по запросу '{query}' не найдены.")


def display_books() -> None:
    """Выводит список всех книг."""
    books = load_books()
    if books:
        for book in books:
            print(book)
    else:
        print("Библиотека пуста.")


def change_status(book_id: int, new_status: str) -> None:
    """Изменяет статус книги."""
    if new_status not in ['в наличии', 'выдана']:
        print("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
        return
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['status'] = new_status
            save_books(books)
            print(f"Статус книги с id {book_id} изменен на '{new_status}'.")
            return
    print(f"Книга с id {book_id} не найдена.")


def print_menu() -> None:
    """Выводит меню программы."""
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Искать книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("6. Выйти")


def main() -> None:
    """Основная функция программы."""
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = input("Введите год издания книги: ").strip()
            add_book(title, author, year)
        elif choice == '2':
            try:
                book_id = int(input("Введите id книги, которую нужно удалить: ").strip())
                delete_book(book_id)
            except ValueError:
                print("Некорректный id.")
        elif choice == '3':
            field = input("Введите поле для поиска (title, author, year): ").strip()
            query = input("Введите запрос для поиска: ").strip()
            if field in ['title', 'author', 'year']:
                search_books(query, field)
            else:
                print("Некорректное поле для поиска.")
        elif choice == '4':
            display_books()
        elif choice == '5':
            try:
                book_id = int(input("Введите id книги: ").strip())
                new_status = input("Введите новый статус (в наличии, выдана): ").strip()
                change_status(book_id, new_status)
            except ValueError:
                print("Некорректный id.")
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
