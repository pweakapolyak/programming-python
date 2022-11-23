from datetime import datetime


class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        """
        :type guid: str
        :type title: str
        :type description: str
        :type link: str
        :type pubdate: datetime
        """
        self.__guid = guid
        self.__title = title
        self.__description = description
        self.__link = link
        self.__pubdate = pubdate

    def get_guid(self):
        return self.__guid

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_link(self):
        return self.__link

    def get_pubdate(self):
        return self.__pubdate
