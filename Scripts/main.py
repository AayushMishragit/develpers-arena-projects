print("PERSONAL PRODUCTIVITY SUITE")

# Open with explicit UTF-8 encoding to avoid UnicodeDecodeError on Windows

print("MAIN MENU:\n1. Calculator Tool\n2. Notes Manager\n3. Timer & Stopwatch\n4.Currency Converter \n5. File Organizer\n6. Exit")
choice = int(input("Select a tool(choose from 1-6):"))
match choice:
    case 1:
        with open("calculator.py", 'r', encoding='utf-8') as f:
            exec(f.read())
    case 2:
        with open('notes.py', 'r', encoding='utf-8') as f:
            exec(f.read())  # Added parentheses to call read() correctly
    case 3:
        with open('timer_sw.py', 'r', encoding='utf-8') as f:
            exec(f.read())
    case 4:
        with open('unit_convertor.py', 'r', encoding='utf-8') as f:
            exec(f.read())
    case 5:
        with open('file_organizer.py', 'r', encoding='utf-8') as f:
            exec(f.read())
    case 6:
        print("Terminated🔚")
        exit()
        


