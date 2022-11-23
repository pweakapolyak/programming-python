from story import NewsStory
from triggers import *


def filter_stories(stories, triggers):
    """
    :type stories: list[NewsStory]
    :type triggers: list[Trigger]
    :return list of filtered NewsStory
    """
    if not triggers:
        return stories

    filtered_stories = []
    for s in stories:
        for t in triggers:
            if t.check_story(s):
                filtered_stories.append(s)
                break

    return filtered_stories


# TODO: implement this method
def read_trigger_config(filename):
    """
    :param filename: filename of trigger configuration
    :type filename: str
    :return: list of Triggers that you parsed from filed
    """

    lines = []
    with open(filename, 'r') as trigger_file:
        for line in trigger_file:
            line = line.rstrip()
            if not (len(line) == 0 or line.startswith('//')):
                lines.append(line)
    if not lines:
        return []

    result_triggers = []
    temp_dict = {}

    for line in lines:
        try:
            cols = line.split(",")
            if cols[0] == "ADD":
                for i in range(1, len(cols)):
                    result_triggers.append(temp_dict[cols[i]])
            else:
                trigger = None

                if cols[1] == "TITLE":
                    trigger = TitleTrigger(cols[2])
                elif cols[1] == "DESCRIPTION":
                    trigger = DescriptionTrigger(cols[2])
                elif cols[1] == "AFTER":
                    trigger = AfterTrigger(cols[2])
                elif cols[1] == "BEFORE":
                    trigger = BeforeTrigger(cols[2])
                elif cols[1] == "NOT":
                    trigger = NotTrigger(temp_dict[cols[2]])
                elif cols[1] == "AND":
                    trigger = AndTrigger(temp_dict[cols[2]], temp_dict[cols[3]])
                elif cols[1] == "OR":
                    trigger = OrTrigger(temp_dict[cols[2]], temp_dict[cols[3]])
                else:
                    raise Exception("Command " + cols[1] + " is not supported")

                temp_dict[cols[0]] = trigger
        except KeyError as e:
            print("Error in line: ", line)
            print('Trigger not found by name, ', e)
        except IndexError as e:
            print("Error in line: ", line)
            print('Not enough parameters for command')
        except Exception as e:
            print('Error in line: ', line)
            print('Unhandled exception: ', e)

    return result_triggers
