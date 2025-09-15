import pathlib

import markdown

from js import console

from puepy import Page, t
from puepy.core import html

from common import app, topics

home = pathlib.Path(__file__).parent 

@app.page("/topics/<topic_id>")
class TopicPage(Page):
    props = ["topic_id"]

    def on_tab_click(self, event):
        panel = event.currentTarget.getAttribute("panel")
        if panel and self.application.state.get("active-topic") != panel:
            self.application.state["active-topic"] = panel
            self.redraw()

    def populate(self):
        topic = next((row for row in topics if row.get("path") == self.topic_id), None)
        valid_ids = [subtopic["id"] for subtopic in topic.get("subtopics", [])]
        active_id = self.application.state.get("active-topic")
        
        if active_id not in valid_ids and valid_ids:
            active_id = valid_ids[0]
            self.application.state["active-topic"] = active_id

        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree(current_topic_path=self.topic_id)

            with t.div():
                t.h2(topic.get("name"))
                with t.wa_tab_group(placement="bottom", active=active_id):
                    for sub_topic in topic.get("subtopics"):
                        tab = t.wa_tab(sub_topic["name"], 
                                       panel=sub_topic["id"],
                                       on_click=self.on_tab_click)
                        #tab.trigger_event
                        with t.wa_tab_panel(name=sub_topic["id"]):
                            subtopic_path = home / f"{sub_topic['id']}.md"
                            raw_html = markdown.markdown(subtopic_path.read_text(), extensions=['extra'])
                            t(html(raw_html))
        t.workshop_footer()



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

 


