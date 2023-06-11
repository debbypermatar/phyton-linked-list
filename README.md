# phyton-linked-list
no 1
membuat program menggunakan single linked list untuk menambahkan tugas baru berdasarkan prioritas seperti ini :
# Menambahkan tugas
task_list.add_task("Mengerjakan tugas matematika", 2)
task_list.add_task("Menulis laporan proyek", 1)
task_list.add_task("Membaca buku", 3)

# Mencetak daftar tugas
task_list.print_tasks_by_priority()

# Menghapus tugas
task_list.remove_task("Menulis laporan proyek")

# Mencetak daftar tugas setelah menghapus
task_list.print_tasks_by_priority()
no 2
membuat program lagi untuk mencatat nama pengunjung
dan judul buku yang di pinjam program tersebut harus bisa mencetak daftar buku yang di pinjam menggunakan program sperti ini :
library = Library()

# Menambahkan pengunjung
library.add_visitor("wawa")
library.add_visitor("ujang")
library.add_visitor("Mamat")

# Menyimpan catatan peminjaman buku
wawa = library.find_visitor("wawa")
wawa.borrow_book("mencintai dia")
wawa.borrow_book("kapan kamu suka sama aku?")

ujang = library.find_visitor("ujang")
ujang.borrow_book("jatuh cinta sendiri")

# Mencetak daftar buku yang dipinjam oleh pengunjung
wawa.print_borrowed_books()
ujang.print_borrowed_books()
