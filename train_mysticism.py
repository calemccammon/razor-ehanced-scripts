skill = Player.GetSkillValue('Mysticism')
manaCost = 0

if skill < 120.0:
    Spells.CastMysticism('Nether Cyclone')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 50
    Misc.Pause(2250)

if Player.Mana < manaCost:
    Player.UseSkill('Meditation')
    Misc.Pause(10000)