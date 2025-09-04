from puepy import Page, t

from common import app

@app.page("/challenges/")
class ChallengesUsingLlms(Page):

    def bias_and_ai_tab(self):
        with t.wa_tab_panel(name="bias-ai"):
            t.h3("Bias and AI")

    def carbon_footprint_tab(self):
        with t.wa_tab_panel(name="carbon-footprint"):
            t.h3("Carbon Footprint")


    def creator_attribution_copyright_tab(self):
        with t.wa_tab_panel(name="attribution-copyright"):
            t.h3("Creator Attribution & Copyright")
    

    def deepfakes_ai_slop(self):
        with t.wa_tab_panel(name="deepfakes-ai-slop"):
            t.h3("Deepfakes & AI Slop")

    def hallucinations_tab(self):
        with t.wa_tab_panel(name="hallucinations"):
            t.h3("Hallucinations")


    def pdoom_agi_tab(self):
        with t.wa_tab_panel(name="pdoom-agi"):
            t.h3("p(doom) & AGI")

    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 t.h2("Challenges with using LLMs")
                 self.sub_topics_tabs()
        
    def privacy_concerns_tab(self):
        with t.wa_tab_panel(name="privacy-concerns"):
            t.h3("Privacy Concerns")


    def sub_topics_tabs(self):
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("Bias and AI", panel="bias-ai")
            t.wa_tab("Creator Attribution & Copyright", panel="attribution-copyright")
            t.wa_tab("Privacy Concerns", panel="privacy-concerns")
            t.wa_tab("Carbon Footprint", panel="carbon-footprint")
            t.wa_tab("Deepfakes & AI Slop", panel="deepfakes-ai-slop")
            t.wa_tab("Hallucinations", panel="hallucinations")
            t.wa_tab("p(doom) & AGI", panel="pdoom-agi")
            self.bias_and_ai_tab()
            self.creator_attribution_copyright_tab()
            self.privacy_concerns_tab()
            self.carbon_footprint_tab()
            self.hallucinations_tab()
            self.pdoom_agi_tab()

