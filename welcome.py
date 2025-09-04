from puepy import Page, t
from common import app, topics

@app.page("/", name="welcome")
class WolfconPage(Page):

    def iching_tab(self):
        with t.wa_tab_panel(name="iching"):
            with t.div():
                t.h3("I-Ching Exercise")

    def sub_topics_tabs(self):
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("Welcome", panel="welcome")
            t.wa_tab("Topics", panel="topics")
            t.wa_tab("Workshop Structure", panel="structure")
            t.wa_tab("iChing Exercise", panel="iching")
            self.welcome_tab()
            self.workshop_topics_tab()
            self.workshop_structure_tab()
            self.iching_tab()


    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                t.h2("Welcome to the Using Generative AI in FOLIO Workshop")
                self.sub_topics_tabs()
     
        with t.wa_dialog(label="About", id="about-dialog"):
              t("The content and source code for this website is licensed under CC0 and the Apache2 license respectively.")
              t.wa_button("Close", slot="footer", varient="brand", data_dialog="close")
        t.wa_button("About", data_dialog="open about-dialog")


    def welcome_tab(self):
        with t.wa_tab_panel(name="welcome"):
            with t.div():
                t.h3("Welcome!")
                t.div("This 1/2 day workshop will cover using Generative AI within FOLIO.")

    def workshop_structure_tab(self):
        with t.wa_tab_panel(name="structure"):
            with t.div():
                t.h3("Structure of the Workshop")
                t.div("We will cover topics 1-2 first, than a ten minute break, followed by topics 3-4, then another break, and finishing with the final topics")

    def workshop_topics_tab(self):
        with t.wa_tab_panel(name="topics"):
            with t.div():
                t.h3("Topics covered in this Workshop")
                with t.ul():
                    for topic in topics:
                        t.li(topic.get('name'))
