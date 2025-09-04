from puepy import Page, t
from common import app

@app.page("/mcp-introduction/")
def MCPIntroduction(Page):

    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 t.h2("Introduction to Model Context Protocol")
                 self.sub_topics_tabs()

    def sub_topics_tabs(self):
        pass

