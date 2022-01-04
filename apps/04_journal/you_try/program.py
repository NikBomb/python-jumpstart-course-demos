import os.path

import journal
from os import path


def main():
    print_header()
    run_event_loop()


def print_header():
    print("----------------")
    print(" JOURNAL APP")
    print("----------------")


def run_event_loop():
    cmd = None
    current_journal = None
    current_journal_path = input("Insert path to journal or create [N]ew")
    journal_name = "Journal"

    if current_journal_path.lower().strip() == "n":
        journal_name = input("Journal Name: ")
        current_journal = []
    elif path.exists(current_journal_path):
        current_journal = journal.load(current_journal_path)
    else:
        print("File not found")
        return

    while cmd != "x":
        cmd = input("[A]dd entry, [L]ist entries, E[x]it: ")
        cmd = cmd.lower().strip()
        if cmd == "a":
            entry = input("Add new entry: ")
            journal.add(current_journal, entry)
        elif cmd == "l":
            journal.list(current_journal)
        elif cmd == "x":
            break
        else:
            print("Operation not implemented")

    savePath = os.path.join(os.getcwd(), "journals")
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    savePath = os.path.join(savePath,journal_name + ".jrl")

    journal.save(savePath, current_journal)


if __name__ == "__main__":
    main()
