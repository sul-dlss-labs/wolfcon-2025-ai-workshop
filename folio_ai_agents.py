from puepy import Page, t
from common import app

@app.page("/folio-ai-agents/")
class FolioAiAgents(Page):

    def ai_agents_tab(self):
        with t.wa_tab_panel(name="ai-agents"):
            t.h3("What are AI Agents?")


    def circ_agent_tab(self):
        with t.wa_tab_panel(name="circ-agent"):
            t.h3("Circulation Agents")


    def edge_ai_tab(self):
        with t.wa_tab_panel(name="edge-ai-module"):
            t.h3("Edge-AI Module")

    def inventory_agent_tab(self):
        with t.wa_tab_panel(name="inventory-agent"):
            t.h3("Inventory Agents")


    def invoice_agent_tab(self):
        with t.wa_tab_panel(name="invoice-agent"):
            t.h3("Invoice Agents")


    def populate(self):
        t.workshop_header()
        t.wa_divider()
        with t.div(classes=["wa-flank", "wa-align-items-start"]):
            with t.div(class_name="wa-split:column"):
                t.topics_tree()

            with t.div():
                 t.h2("FOLIO AI Agents")
                 self.sub_topics_tabs()


    def sub_topics_tabs(self):
        with t.wa_tab_group(placement="bottom"):
            t.wa_tab("AI Agents", panel="ai-agents")
            t.wa_tab("Edge-AI Module", panel="edge-ai-module")
            t.wa_tab("Inventory Agent", panel="inventory-agent")
            t.wa_tab("Invoice Agent", panel="invoice-agent")
            t.wa_tab("Circulation Agent", panel="circ-agent")
            self.ai_agents_tab()
            self.edge_ai_tab()
            self.inventory_agent_tab()
            self.invoice_agent_tab()
            self.circ_agent_tab()   

