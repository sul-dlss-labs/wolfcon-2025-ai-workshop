from puepy import Page, t
from common import app


@app.page("/intro-llms-ai/")
class IntroductionLlmsAi(Page):

    def sub_topics_tabs():
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("")


    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 self.sub_topics_tabs()