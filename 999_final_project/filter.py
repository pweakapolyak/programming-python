from story import NewsStory



# TODO: implement this method
def filter_stories(stories):
    """
    :type stories: list[NewsStory]
    :return list of filtered NewsStory
    """
    triggers = read_trigger_config("trigger_config.txt")
    # TODO: filter stories by triggers
    return stories


# TODO: implement this method
def read_trigger_config(filename):
    """
    :param filename: filename of trigger configuration
    :type filename: str
    :return: list of Triggers that you parsed from filed
    """
