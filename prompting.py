from puepy import Page, t
from common import app

@app.page("/prompt-engineering/")
class PromptingLLMs(Page):


    def automatic_prompt_generation(self):
        with t.wa_tab_panel(name="auto-generated"):
            t.h3("Automatically Generated")

    def chain_of_thought(self):
        with t.wa_tab_panel(name="cot"):
            t.h3("Chain-of-Thought Technique")

    def combining_techniques(self):
        with t.wa_tab_panel(name="combining-techniques"):
            t.h3("Combining Prompt Techniques")


    def multi_shot_tab(self):
        with t.wa_tab_panel(name="multi-shot"):
            t.h3("Multi-Shot or Examples")


    def overview_tab(self):
        with t.wa_tab_panel(name="overview"):
            t.h3("Overview")


    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 t.h2("Prompt Engineering for FOLIO")
                 self.sub_topics_tabs()


    def sub_topics_tabs(self):
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("Overview", panel="overview")
            t.wa_tab("Zero Shot", panel="zero-shot")
            t.wa_tab("Multi-shot", panel="multi-shot")
            t.wa_tab("Chain-of-Thought", panel="cot")
            t.wa_tab("Automatically Generated", panel="auto-generated")
            t.wa_tab("Combining Techniques", panel="combining-techniques")
            self.overview_tab()
            self.zero_shot_tab()
            self.multi_shot_tab()
            self.chain_of_thought()
            self.automatic_prompt_generation()
            self.combining_techniques()

    def zero_shot_tab(self):
        with t.wa_tab_panel(name="zero-shot"):
            t.h3("Zero Shot Prompts")

