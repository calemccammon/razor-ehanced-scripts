stepCount = int(Player.GetSkillValue('Stealth') * 2.0 / 10.0)

Journal.Clear()
Player.Walk('East')
Misc.Pause(300)
Player.UseSkill('Hiding')
Misc.Pause(1000)
Player.Walk('East')
Misc.Pause(1000)
if(Journal.Search('You begin to move quietly.')):
    Misc.SendMessage(str(stepCount))
    Journal.Clear()
    Player.Walk('West')
    divFour = stepCount / 4
    while(stepCount != 0):
        Misc.Pause(300)
        for x in range(divFour):
            Player.Walk('West')
            Misc.Pause(300)
            stepCount = stepCount - 1
        
        Player.Walk('North')
        Misc.Pause(300)
        for x in range(divFour):
            Player.Walk('North')
            Misc.Pause(300)
            stepCount = stepCount - 1
            
        Player.Walk('East')
        Misc.Pause(300)
        for x in range(divFour):
            Player.Walk('East')
            Misc.Pause(300)
            stepCount = stepCount - 1
        for x in range(divFour):
            Player.Walk('South')
            Misc.Pause(300)
            stepCount = stepCount - 1
            
        Player.Walk('West')
        Misc.Pause(300)
            
            
    