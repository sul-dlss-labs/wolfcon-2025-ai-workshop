import pathlib

import markdown

from puepy import Page, t
from puepy.core import html

from common import app, topics

home = pathlib.Path(__file__).parent 

@app.page("/topics/<topic_id>")
class TopicPage(Page):
    props = ["topic_id"]

    def populate(self):
        for row in topics:
            if row.get("path") == self.topic_id:
                topic = row
                break
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                t.h2(topic.get("name"))
                with t.wa_tab_group(placement="bottom"):
                    for sub_topic in topic.get("subtopics"):
                        t.wa_tab(sub_topic["name"], panel=sub_topic["id"])
                        with t.wa_tab_panel(name=sub_topic["id"]):
                            subtopic_path = home / f"{sub_topic['id']}.md"
                            raw_html = markdown.markdown(subtopic_path.read_text(), extensions=['extra'])
                            t(html(raw_html))



@app.page()
class DefaultPage(Page):
    def populate(self):
       t.workshop_header()
       t.wa_divider()
       with t.div(classes=["wa-flank", "wa-align-items-start"]):
           with t.div(class_name="wa-split:column"):
               t.topics_tree()

           with t.div():
                t.h2("Welcome to the Using Generative AI in FOLIO Workshop")

 


