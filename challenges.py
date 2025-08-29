from puepy import Page, t

from common import app, topics

@app.page("/challenges/")
class ChallengesUsingLlms(Page):

    def populate(self):
        t.workshop_header()
        t.wa_divider()
        t.h1(f"{topics[2].get('name')}")


