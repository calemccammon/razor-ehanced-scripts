key = Items.FindByID(0x100E, -1, Player.Backpack.Serial)
container = Items.FindByID(0x09A9, -1, Player.Backpack.Serial)
pick = Items.FindByID(0x14FB, -1, Player.Backpack.Serial)

if pick != None:
    Journal.Clear()
    Items.UseItem(pick)
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(container)
    Misc.Pause(1250)
    if Journal.Search("quickly yields") or Journal.Search("appear to be locked"):
        Items.UseItem(key)
        Target.WaitForTarget(5000, False)
        Target.TargetExecute(container)
        Misc.Pause(1250)