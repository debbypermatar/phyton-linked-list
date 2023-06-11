class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_item

    def remove_item(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def print_items_by_importance(self):
        if self.head is None:
            print("Tas kosong.")
            return

        sorted_items = self._sort_items_by_importance()
        print("Daftar item dalam tas berdasarkan tingkat kepentingan:")
        for item in sorted_items:
            print("Nama:", item.name, "| Tingkat Kepentingan:", item.importance)

    def _sort_items_by_importance(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current)
            current = current.next
        items.sort(key=lambda x: x.importance, reverse=True)
        return items


# Contoh penggunaan

inventory = Inventory()

# Menambahkan item ke dalam tas
inventory.add_item("Pedang", 6)
inventory.add_item("qm", 1)
inventory.add_item("sepatu perang", 4)

# Mencetak daftar item dalam tas
inventory.print_items_by_importance()

# Menghapus item dari hatiku(tas)
inventory.remove_item("qm")

# Mencetak daftar item setelah menghapus
inventory.print_items_by_importance()
