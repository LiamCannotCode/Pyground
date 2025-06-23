def total_xp(level, xp_to_add):
    level_xp = level * 100
    total_xp = level_xp + xp_to_add
    return level, level_xp, total_xp

print(total_xp(2, 69))
