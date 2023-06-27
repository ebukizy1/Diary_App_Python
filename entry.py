class Entry:

    def __init__(self, title, body):
        self.__title = title
        self.__body = body
        self.__ID = None


    @property
    def entry_ID(self):
        return self.__ID

    @entry_ID.setter
    def entry_ID(self, ID):
        self.__ID = ID

    @property
    def entry_title(self):
        return self.__title

    @entry_title.setter
    def entry_title(self, title):
        self.__title = title

    @property
    def entry_body(self):
        return self.__body

    @entry_body.setter
    def entry_body(self, body):
        self.__body = body

    def __str__(self):
        return f" TITLE : {self.__title}" \
               f" BODY  : {self.__body} "


