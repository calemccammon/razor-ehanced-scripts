Spells.CastSpellweaving('Word Of Death')
Target.WaitForTarget(10000)
Target.Self()
if Player.Mana <= 50:
    Misc.Pause(3000)
    Player.UseSkill('Meditation')
    Misc.Pause(15000)
if Player.Hits <= 50:
    Misc.Pause(3000)
    Spells.CastMagery('Greater Heal')
    Target.WaitForTarget(10000)
    Target.Self()
Misc.Pause(3000)