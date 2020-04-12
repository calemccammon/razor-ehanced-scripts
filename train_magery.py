magery = Player.GetSkillValue('Magery')
manaCost = 0;

if(magery < 80.0):
    Spells.CastMagery('Invisibility')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 20
    Misc.Pause(5000)
elif (magery < 95.0):
    Spells.CastMagery('Mass Dispel')
    Target.WaitForTarget(10000)
    Target.Self()
    manaCost = 40
    Misc.Pause(5000)
    
if(Player.Mana < manaCost):
    Player.UseSkill('Meditation')
    Misc.Pause(15000)