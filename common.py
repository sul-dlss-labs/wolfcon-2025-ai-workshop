from js import console

from puepy import Application, Component, t
from puepy.core import html
from puepy.router import Router


topics = [
    {"name": "Workshop Welcome",
     "path": "welcome",
     "subtopics": [
         {"name": "Welcome", "id": "welcome"},
         {"name": "Topics Covered", "id": "topics"},
         {"name": "Workshop Structure", "id": "structure"},
         {"name": "IChing Exercise", "id": "iching"}
     ]},
    {"name": "Introduction to AI and LLMs",
     "path": "intro-llms-ai",
     "subtopics": [
         {"name": "Overview of AI", "id": "ai-overview"},
         {"name": "Neural Nets & Transformers", "id": "nn-transformers"},
         {"name": "LLMs and MLLMs", "id": "llms"},
         {"name": "Commercial LLMs", "id": "commercial-llms"},
         {"name": "Open Source LLMs", "id": "open-source-llms"}
    ]},
    {"name": "Prompt Engineering for FOLIO",
      "path": "prompt-engineering",
      "subtopics": [
          {"name": "Overview", "id": "prompt-overview"},
          {"name": "Zero Shot", "id": "zero-shot"},
          {"name": "Multi-shot", "id": "multi-shot"},
          {"name": "Chain-of-Thought", "id": "cot"},
          {"name": "Using with RAG", "id": "rag" },
          {"name": "Combining Techniques", "id": "combining-techniques"}
      ]},
    {"name": "Challenges with using LLMs",
     "path": "challenges",
     "subtopics": [
         {"name": "Bias and AI", "id": "bias-ai"},
         {"name": "Creator Attribution & Copyright", "id": "attribution-copyright"},
         {"name": "Privacy Concerns", "id": "privacy-concerns"},
         {"name": "Carbon Footprint", "id": "carbon-footprint"},
         {"name": "Deepfakes & AI Slop", "id": "deepfakes-ai-slop"},
         {"name": "Hallucinations", "id": "hallucinations"},
         {"name": "p(doom) & AGI", "id": "pdoom-agi"}
     ]},
    {"name": "FOLIO AI Agents",
      "path": "folio-ai-agents",
      "subtopics": [
          {"name": "AI Agents", "id": "ai-agents"},
          {"name": "Edge-AI Module", "id": "edge-ai-module"},
          {"name": "Inventory Agent", "id": "inventory-agent"},
          {"name": "Invoice Agent", "id": "invoice-agent"},
      ]},
    {"name": "Introduction to MCP",
      "path": "mcp-introduction",
      "subtopics": [
          {"name": "What is MCP?", "id": "what-mcp"},
          {"name": "Clients", "id": "mcp-clients"},
          {"name": "Servers", "id": "mcp-servers"},
          {"name": "Examples", "id": "mcp-examples"}
      ]},
    {"name": "MCP Client/Servers for FOLIO Apps",
      "path": "folio-mcp-client-servers",
      "subtopics": [
          {"name": "Edge-AI as a MCP Server", "id": "edge-ai-mcp-server"},
          {"name": "Using with Claude Desktop", "id": "using-claude-desktop"}
      ]},
    {"name": "Wrap-up & Sources",
      "path": "wrap-up-sources",
      "subtopics": [
          {"name": "Wrap-up & Final Thoughts", "id": "wrap-up-final-thoughts"},
          {"name": "Sources", "id": "sources"}
      ]
    }
]


@t.component()
class TopicsTree(Component):
    redraw_on_changes = True
    props = ["current_topic_path"]

    def topic_tree_item(self, topic):
        topic_path = topic.get("path", "")
        
        is_current_topic = (self.current_topic_path == topic_path)

        with t.wa_tree_item(topic.get("name", "Missing Topic Name"), expanded=is_current_topic): 
            for sub_topic in topic.get("subtopics"):
                sub_id = sub_topic.get("id")
                is_active = self.application.state.get("active-topic") == sub_id
                if is_active:
                    tree_item = t.wa_tree_item(
                      sub_topic.get("name"),
                      selected=True
                    )
                else:
                    t.wa_tree_item(
                        t.a(sub_topic.get("name", "Missing subtopic Name"),
                            on_click=self.show_subtopic,
                            data_subtopic_id=sub_topic.get("id"), 
                            href=f"#topics/{topic_path}")
                    )


    def populate(self):
        with t.wa_tree(class_name="tree-with-lines"):
            for topic in topics:
                self.topic_tree_item(topic)

    def show_subtopic(self, event):
        sub_id = event.currentTarget.getAttribute("data-subtopic-id")
        if sub_id:
            self.application.state["active-topic"] = sub_id
            self.redraw()

@t.component()
class WorkshopHeader(Component):

    def populate(self):
        with t.div(class_name="wa-flank", style="--flank-size: 8rem"):
            with t.div(classes=["wa-frame", "wa-border-radius-m"]):
                t.img(src="imgs/WOLFcon-2025-logo-2.png", style="width: 150px", alt="WOLFcon 2025 Logo")
            with t.div(class_name="wa-flank:end", style="--content-percentage: 70%"):
                with t.div(classes=["wa-stack", "wa-gap-xs"]):
                    t.h1("Using Generative AI with FOLIO")
                    t.span(html("Jeremy Nelson<br>Stanford University Libraries"))


@t.component()
class WorkshopFooter(Component):

    def populate(self):
        with t.div(classes="container"):
            t.wa_divider()
            t.p("The content and source code for this website is licensed under CC0 and the Apache2 license respectively.")           

app = Application()
app.install_router(Router, link_mode=Router.LINK_MODE_HASH)
