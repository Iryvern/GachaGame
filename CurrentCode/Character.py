class Character:
    def __init__(self, name, rarity, level=1, experience=0, char_class="Warrior", personality="Neutral", growth_potential=1, strength=10, intelligence=10, health=100, agility=10, food=100, water=100, stamina=100, sanity=100, skills=None):
        self.name = name
        self.rarity = rarity
        self.level = level
        self.experience = experience
        self.char_class = char_class
        self.personality = personality
        self.growth_potential = growth_potential
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.agility = agility
        self.food = food
        self.water = water
        self.stamina = stamina
        self.sanity = sanity
        self.skills = skills or []

    def level_up(self):
        self.level += 1
        # Example growth - adjust based on character's growth potential
        self.strength += 2
        self.intelligence += 2
        self.health += 20
        self.agility += 2
        # Potentially update experience, skills, etc.

    def add_experience(self, amount):
        self.experience += amount
        # Implement logic for leveling up based on experience if desired

    def consume_resources(self):
        # Example method to simulate consumption and need for resources
        self.food -= 10
        self.water -= 10
        self.stamina -= 10
        self.sanity -= 5  # Adjust these values based on game mechanics

    def rest(self):
        # Example method to recover stamina and sanity
        self.stamina = min(100, self.stamina + 20)
        self.sanity
