class Npcs():
    def __init__(self, name, npc_enemy, dialouge=None):
        self.name = name
        self.npc_enemy = npc_enemy
        self.dialouge = dialouge or []

