class Location:
    def __init__(self, name, description, exits=None, enemies=None, npcs=None):
        self.name = name
        self.description = description
        self.exits = exits or []
        self.enemies = enemies or []
        self.npcs = npcs or []
