import os


def load(current_journal_path):
    journal_entries = []
    file = open(current_journal_path)
    entries = file.readlines()
    for entry in entries:
        journal_entries.append(entry.strip())
    return journal_entries


def add(current_journal: list, entry):
    current_journal.append(entry)
    return


def list(current_journal: list):
    for idx, entry in enumerate(reversed(current_journal)):
        print("{}) {}".format(idx, entry))


def save(savePath, current_journal):
    with open(savePath, "w") as fout:
        for entry in current_journal:
            fout.write(entry + "\n")
