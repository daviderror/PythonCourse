pages = 100                # количество страниц
lines_per_page = 50       # число строк на странице
chars_per_line = 25       # количество символов в строке
bytes_per_char = 4        # объем одного символа в байтах

# Объем дискеты в байтах
disk_size_mb = 1.44       # объем дискеты в мегабайтах
disk_size_bytes = disk_size_mb * 1024 * 1024  # перевод в байты

# Объем одной книги в байтах
total_chars = pages * lines_per_page * chars_per_line
book_size_bytes = total_chars * bytes_per_char

# Количество книг, которое можно поместить на дискету
num_books = disk_size_bytes // book_size_bytes

# Преобразуем в целое число
num_books = int(num_books)

# Вывод результата
print("Количество книг, помещающихся на дискету:", num_books)