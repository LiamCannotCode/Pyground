def take_magic_damage(health, resist, amp, spell_power):
    combined_damage = spell_power * amp
    combined_health = health + resist
    new_health = combined_health - combined_damage
    return new_health

