magery = Player.GetSkillValue('Magery')
manaCost = 0

if magery < 55.0:
    Spells.CastMagery('Magic Reflection')
    manaCost = 14
    Misc.Pause(5000)
if magery < 75.0:
    Spells.CastMagery('Invisibility')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 20
    Misc.Pause(1750)
elif magery < 90.0:
    Spells.CastMagery('Mass Dispel')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 40
    Misc.Pause(2000)
elif magery < 120.0:
    Spells.CastMagery('Earthquake')
    manaCost = 50
    Misc.Pause(5000)
    
if(Player.Mana < manaCost):
    Player.UseSkill('Meditation')
    Misc.Pause(15000)