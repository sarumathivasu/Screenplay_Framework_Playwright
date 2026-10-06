class Actor:
    def __init__(self,name):
        self.name=name
        self.abilities={}

    def can(self,ability):
        self.abilities(type(ability))=ability
        # type(ability) -- "Find out which Ability class this object belongs to and use that class as the key."

actor=Actor("sarumathi")

