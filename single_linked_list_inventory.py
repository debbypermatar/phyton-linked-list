class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.code == code:
                current.next = current.next.next
                return
            current = current.next

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
            return

        print("Daftar produk dalam inventaris:")
        current = self.head
        while current is not None:
            print("Nama:", current.name, "| Kode:",
                  current.code, "| Jumlah Stok:", current.stock)
            current = current.next


# Contoh penggunaan

inventory = InventoryManagement()

# Menambahkan produk ke dalam inventaris
inventory.add_product("Buku", "BB001", 10)
inventory.add_product("map", "MM001", 30)
inventory.add_product("kertas", "KK001", 25)

# Mencetak daftar produk dalam inventaris
inventory.print_inventory()

# Menghapus produk dari inventaris
inventory.remove_product("BB001")

# Mencetak daftar produk setelah menghapus
inventory.print_inventory()
