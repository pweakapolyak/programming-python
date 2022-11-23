import string
from datetime import datetime

from story import NewsStory


class Trigger:
    def check_story(self, story):
        """
        Returns True if story is accepted by trigger
        :type story: NewsStory
        :return: boolean
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.__phrase = phrase.lower()

    def is_phrase_in(self, text):
        """
        :type text: str
        """
        text_without_punctuation = text.lower()
        for p in string.punctuation:
            text_without_punctuation = text_without_punctuation.replace(p, " ")

        text_words = self.__extract_words(text_without_punctuation)
        phrase_words = self.__extract_words(self.__phrase)

        return self.__is_sublist_in_list(text_words, phrase_words)

    def __extract_words(self, text):
        return [x for x in text.split(" ") if x != ""]

    def __is_sublist_in_list(self, list, sublist):
        n = len(list)
        m = len(sublist)
        for i in range(n - m + 1):
            found = True
            for j in range(m):
                if list[i + j] != sublist[j]:
                    found = False
                    break
            if found:
                return True
        return False


class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def check_story(self, story):
        return super().is_phrase_in(story.get_title())


class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def check_story(self, story):
        return super().is_phrase_in(story.get_description())


class TimeTrigger(Trigger):
    def __init__(self, time_as_str):
        self.__datetime = datetime.strptime(time_as_str, "%d %b %Y %H:%M:%S")

    def get_datetime(self):
        return self.__datetime


class BeforeTrigger(TimeTrigger):
    def __init__(self, time_as_str):
        super().__init__(time_as_str)

    def check_story(self, story):
        return super().get_datetime() > story.get_pubdate()


class AfterTrigger(TimeTrigger):
    def __int__(self, time_as_str):
        super().__init__(time_as_str)

    def check_story(self, story):
        return super().get_datetime() < story.get_pubdate()


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.__trigger = trigger

    def check_story(self, story):
        return not self.__trigger.check_story(story)


class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.__trigger1 = trigger1
        self.__trigger2 = trigger2

    def check_story(self, story):
        return self.__trigger1.check_story(story) and self.__trigger2.check_story(story)


class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.__trigger1 = trigger1
        self.__trigger2 = trigger2

    def check_story(self, story):
        return self.__trigger1.check_story(story) or self.__trigger2.check_story(story)
