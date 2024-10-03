import json

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}: {task}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List:")
        todo_list.view_tasks()
        print("\nOptions: [a]dd, [u]pdate, [d]elete, [v]iew, [q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == 'u':
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == 'd':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == 'v':
            todo_list.view_tasks()
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
