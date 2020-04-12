skill = Player.GetSkillValue('Ninjitsu')
Journal.Clear()

if(skill < 50.1):
    Spells.CastNinjitsu("Animal Form")
    Gumps.WaitForGump(9014, 10000)
    Gumps.SendAction(9014, 102 if skill >= 50.0 else 100)
    Misc.Pause(5000)
    if(not Journal.Search('The spell fizzles.')):
        Spells.CastNinjitsu("Animal Form")
        Misc.Pause(5000)
elif (skill < 86.0):
    if(not Player.BuffsExist('Hiding')):
        Player.UseSkill("Hiding")
        Misc.Pause(1500)
    Player.Walk("East")
    Misc.Pause(1500)
    Spells.CastNinjitsu("Shadowjump")
    Target.WaitForTarget(10000, False)
    Misc.Pause(500)
    Target.TargetExecute(629, 2231 ,0)
    Misc.Pause(1500)
    if not Journal.Search('The spell fizzles.'):
        Player.Walk("West")
    Misc.Pause(1500)
    Player.Walk("West")
    Misc.Pause(1500)
    Player.Walk("West")
    Misc.Pause(1500)
    Player.Walk("East")
    Misc.Pause(1500)