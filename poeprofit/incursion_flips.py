class IncursionFlip:
    def __init__(self, vial, before, after, type):
        self.vial = vial
        self.before = before
        self.after = after
        self.type = type
    def __str__(self):
        return f"Flip for {self.vial}, apply on {self.before} to get {self.after}"


def get_incursion_flips():
    ret = [IncursionFlip("Vial of Awakening", "Apep's Slumber", "Apep's Supremacy", "armour"),
           IncursionFlip("Vial of Consequence", "Coward's Chains", "Coward's Legacy", "accesoires"),
           IncursionFlip("Vial of Dominance", "Architect's Hand", "Slavedriver's Hand", "armour"),
           IncursionFlip("Vial of Fate", "Story of the Vaal", "Fate of the Vaal", "weapon"),
           IncursionFlip("Vial of Summoning", "Mask of the Spirit Drinker", "Mask of the Stitched Demon", "armour"),
           IncursionFlip("Vial of the Ritual", "Dance of the Offered", "Omeyocan", "armour"),
           IncursionFlip("Vial of Sacrifice", "Sacrificial Heart", "Zerphi's Heart", "accesoires"),
           IncursionFlip("Vial of Transcendence", "Tempered Flesh", "Transcendent Flesh", "jewel"),
           IncursionFlip("Vial of Transcendence", "Tempered Spirit", "Transcendent Spirit", "jewel"),
           IncursionFlip("Vial of Transcendence", "Tempered Mind", "Transcendent Mind", "jewel"),
           IncursionFlip("Vial of the Ghost", "Soul Catcher", "Soul Ripper", "flask")
    ]
    return ret
