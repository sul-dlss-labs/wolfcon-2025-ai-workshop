from puepy import Page, t
from common import app


@app.page("/intro-llms-ai/")
class IntroductionLlmsAi(Page):

    def commercial_llms(self):
        with t.wa_tab_panel(name="commercial-llms"):
            t.h3("Commercial LLMs")


    def large_language_models(self):
        with t.wa_tab_panel(name="llms"):
            t.h3("Large Language Models")


    def neural_nets_transformers(self):
        with t.wa_tab_panel(name="nn-transformers"):
            t.h3("Neural Nets & Transformers")


    def open_source_llms(self):
        with t.wa_tab_panel(name="open-source-llms"):
            t.h3("Open Source LLMs")


    def overview_tab(self):
        with t.wa_tab_panel(name="overview"):
            t.h3("Overview of AI")

    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 t.h2("Introduction to AI and LLMs")
                 self.sub_topics_tabs()

    def sub_topics_tabs(self):
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("Overview of AI", panel="overview")
            t.wa_tab("Neural Nets & Transformers", panel="nn-transformers")
            t.wa_tab("Large Language Models", panel="llms")
            t.wa_tab("Commercial LLMs", panel="commercial-llms")
            t.wa_tab("Open Source LLMs", panel="open-source-llms")
            self.overview_tab()
            self.neural_nets_transformers()
            self.large_language_models()
            self.commercial_llms()
            self.open_source_llms()


