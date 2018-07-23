import get_db


class info:
    def readAllInfo(self):
        Events = get_db.getDBEvent()
        News = get_db.getDBNews()
        Wikipedia = get_db.getDBWikipedia()
        return (Events, News, Wikipedia)
