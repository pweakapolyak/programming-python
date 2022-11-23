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


# TODO: implement it
class PhraseTrigger(Trigger):
    pass

# TODO: implement it
class TitleTrigger(PhraseTrigger):
    pass

# TODO: implement it
class DescriptionTrigger(PhraseTrigger):
    pass

# TODO: implement it
class TimeTrigger(Trigger):
    pass

# TODO: implement it
class BeforeTrigger(TimeTrigger):
    pass

# TODO: implement it
class AfterTrigger(TimeTrigger):
    pass

# TODO: implement it
class NotTrigger(Trigger):
    pass

# TODO: implement it
class AndTrigger(Trigger):
    pass

# TODO: implement it
class OrTrigger(Trigger):
    pass
