class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next_task = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current_task = self.head
            while current_task.next_task is not None:
                current_task = current_task.next_task
            current_task.next_task = new_task

    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next_task
            return

        current_task = self.head
        while current_task.next_task is not None:
            if current_task.next_task.description == description:
                current_task.next_task = current_task.next_task.next_task
                return
            current_task = current_task.next_task

    def print_tasks_by_priority(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        sorted_tasks = self._sort_tasks_by_priority()
        print("Daftar tugas berdasarkan prioritas:")
        for task in sorted_tasks:
            print("Deskripsi:", task.description,
                  "| Prioritas:", task.priority)

    def _sort_tasks_by_priority(self):
        tasks = []
        current_task = self.head
        while current_task is not None:
            tasks.append(current_task)
            current_task = current_task.next_task
        tasks.sort(key=lambda x: x.priority, reverse=True)
        return tasks


# Contoh penggunaan

task_list = TaskList()

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
