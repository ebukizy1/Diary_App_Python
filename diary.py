from diary_project.entry import Entry


class Diary:

    def __init__(self, user_name, password):
        self.__isLocked = True
        self.__user_name = user_name
        self.__password = password
        self.__Entry = []

    def isLocked(self):
        return self.__isLocked

    def unlock(self, password):
        if self.__password == password:
            self.__isLocked = False
        else:
            raise TypeError("wrong password enter")

    def create_entry(self, title, body):
        my_entry = Entry(title, body)
        self.__Entry.append(my_entry)
        my_entry.entry_ID = self.generate_ID()

    def generate_ID(self):
        ID = "00" + str(len(self.__Entry))
        return ID

    def check_size_of_list(self):
        return len(self.__Entry)

    def delete_entry(self, ID):
        self.__validate_ID(ID)
        for entry in self.__Entry:
            if ID == entry.entry_ID:
                self.__Entry.remove(entry)
                break

    def __validate_ID(self, ID):
        for entry in self.__Entry:
            if ID == entry.entry_ID:
                return ID

        raise TypeError("ID enter not found in the list of diaries")

    def find_entry(self, ID):
        self.__validate_ID(ID)
        for entry in self.__Entry:
            if ID == entry.entry_ID:
                return entry

    def updateEntry(self,id, title, body):
        for entry in self.__Entry:
            if id == entry.entry_ID:
                entry.entry_title = title
                entry.entry_body = body









