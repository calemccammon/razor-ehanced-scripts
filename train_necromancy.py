skill = Player.GetSkillValue('Necromancy')
manaCost = 0

if skill <= 50.0:
    Spells.CastNecro('Wraith Form')
    manaCost = 17
    Misc.Pause(5000)
elif skill <= 71.0:
    Spells.CastNecro('Horrific Beast')
    manaCost = 11
    Misc.Pause(5000)
elif skill < 87.9:
    Spells.CastNecro('Wither')
    manaCost = 23
    Misc.Pause(5000)
elif skill <= 100.0:
    Spells.CastNecro('Lich Form')
    manaCost = 23
    Misc.Pause(5000)

if Player.Mana < manaCost:
    Player.UseSkill('Meditation')
    Misc.Pause(10000)