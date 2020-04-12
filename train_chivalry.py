skill = Player.GetSkillValue('Chivalry')
manaCost = 0

if skill < 60.0:
    Spells.CastChivalry('Divine Fury')
    manaCost = 15
    Misc.Pause(5000)
elif skill < 70.0:
    Spells.CastChivalry('Enemy Of One')
    manaCost = 20
    Misc.Pause(5000)
elif skill < 90.0:
    Spells.CastChivalry('Holy Light')
    manaCost = 10
    Misc.Pause(5000)
elif skill < 115.0:
    Spells.CastChivalry('Noble Sacrifice')
    manaCost = 20
    Misc.Pause(5000)

if Player.Mana < manaCost:
    Player.UseSkill('Meditation')
    Misc.Pause(10000)