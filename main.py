from puepy import Application, Page, t

app = Application()

topics = [{"name": "Introduction Large Language Models (LLMs) and AI"},
          {"name": "Challenges of using LLMs"},
          {"name": "Prompt Engineering for FOLIO"},
          {"name": "Creating and using FOLIO AI Agents"},
          {"name": "Model Context Protocol (MCP) Server/Client introduction"},
          {"name": "MCP Servers for FOLIO Apps"}]

@app.page()
class WOLFconPage(Page):
    def populate(self):
        with t.div(class_name="wa-flank", style="--flank-size: 8rem"):
            with t.div(classes=["wa-frame", "wa-border-radius-m"]):
                t.img(src="imgs/WOLFcon-2025-logo-2.png", style="width: 150px", alt="WOLFcon 2025 Logo")
            with t.div(class_name="wa-flank:end", style="--content-percentage: 70%"):
                t.h1("Using Generative AI with FOLIO")
                t.span("Jeremy Nelson, Stanford University Libraries")
        with t.wa_tab_group(placement="start"):
            t.wa_tab("Welcome", panel="welcome")
            t.wa_tab("Topics", panel="topics")
            t.wa_tab("Workshop Structure", panel="structure")
            with t.wa_tab_panel(name="welcome"):
                with t.div():
                    t.h2("Welcome to the Using Generative AI in FOLIO Workshop")
                    t.div("This 1/2 workshop will cover using Generative AI within FOLIO.")
            with t.wa_tab_panel(name="topics"):
                with t.div():
                    t.h2("Topics covered in this Workshop")
                    with t.ul():
                        for topic in topics:
                            t.li(topic.get('name'))
            with t.wa_tab_panel(name="structure"):
                with t.div():
                    t.h2("Structure of the Workshop")
                    t.div("We will cover topics 1-2 first, than a ten minute break, followed by topics 3-4, then another break, and finishing with the final topics")
        with t.wa_dialog(label="About", id="about-dialog"):
              t("The content and source code for this website is licensed under CC0 and the Apache2 license respectively.")
              t.wa_button("Close", slot="footer", varient="brand", data_dialog="close")
        t.wa_button("About", data_dialog="open about-dialog")

app.mount("#app")
    
