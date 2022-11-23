from tkinter import *
from tkinter import ttk
from story import NewsStory
from reader import read_latest_news

shown_news = []


def display_not_shown_story(cont, story):
    """
    :type story: NewsStory
    """
    if story.get_guid() not in shown_news:
        cont.insert(END, story.get_title() + "\n", "title")
        cont.insert(END, "\n---------------------------------------------------------------\n", "title")
        cont.insert(END, story.get_description())
        cont.insert(END, "\n*********************************************************************\n", "title")
        shown_news.append(story.get_guid())


def update_news():
    print("Read all news from google . . .")
    stories = read_latest_news("https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru")

    for s in stories:
        display_not_shown_story(content_area, s)
    scrollbar.config(command=content_area.yview)


if __name__ == "__main__":
    root = Tk()
    root.title("RSS Reader")

    frame = ttk.Frame(root, padding=10)
    frame.pack(side=BOTTOM)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    title = StringVar()
    title.set("Google News")
    ttl = Label(root, textvariable=title, font=("Helvetica", 18))
    ttl.pack(side=TOP)

    content_area = Text(root, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
    content_area.pack(side=BOTTOM)
    content_area.tag_config("title", justify='center')

    button = Button(frame, text="Обновить новости", command=update_news)
    button.pack(side=BOTTOM)

    root.mainloop()
