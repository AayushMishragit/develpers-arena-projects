print("=====================================================")
print("NOTES MANAGER")

from datetime import datetime

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        created_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "body": body,
            "created": created_time
        }

        self.notes.append(note)
        print("\n✅ Note added successfully!\n")

    def show_notes(self):
        if not self.notes:
            print("\n⚠️ No notes available.\n")
            return

        print("\n📒 Your Notes:\n")
        for note in self.notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Created: {note['created']}")
            print("-" * 30)

    def delete_note(self):
        if not self.notes:
            print("\n⚠️ No notes to delete.\n")
            return

        self.show_notes()
        try:
            note_id = int(input("\nEnter note ID to delete: "))
            for note in self.notes:
                if note["id"] == note_id:
                    self.notes.remove(note)
                    print("\n🗑️ Note deleted successfully!\n")
                    self.reassign_ids()
                    return
            print("\n❌ Note ID not found.\n")
        except ValueError:
            print("\n❌ Invalid input.\n")

    def reassign_ids(self):
        for index, note in enumerate(self.notes):
            note["id"] = index + 1


def main():
    manager = NotesManager()

    while True:
        print("\n===== Notes Manager =====")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_note()
        elif choice == "2":
            manager.show_notes()
        elif choice == "3":
            manager.delete_note()
        elif choice == "4":
            print("\n👋 Exiting Notes Manager. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
print("=====================================================")    