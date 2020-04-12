skill = Player.GetSkillValue('Spellweaving')
manaCost = 0

if skill < 20.0:
    Spells.CastSpellweaving('Arcane Circle')
    manaCost = 24
    Misc.Pause(5000)
elif skill < 33.0:
    Spells.CastSpellweaving('Immolating Weapon')
    manaCost = 32
    Misc.Pause(5000)
elif skill < 44.0:
    Spells.CastSpellweaving('Reaper Form')
    manaCost = 34
    Misc.Pause(5000)
elif skill < 90.0:
    Spells.CastSpellweaving('Wildfire')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 50
    Misc.Pause(2500)
elif skill < 120.0:
    Spells.CastSpellweaving('Word Of Death')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 50
    Misc.Pause(3500)

if Player.Mana < manaCost:
    Misc.Pause(3000)
    Player.UseSkill('Meditation')
    Misc.Pause(15000)
if Player.Hits < 50:
    Misc.Pause(3000)
    Spells.CastMagery('Greater Heal')
    Target.WaitForTarget(10000)
    Target.Self()