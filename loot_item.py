lootItem = Target.PromptTarget()
if lootItem:
    itemWeight = Items.GetPropValue(lootItem, 'Weight')
    if itemWeight + Player.Weight > Player.MaxWeight:
        Misc.SendMessage('Overburdened')
    else:
        Items.Move(lootItem, Player.Backpack.Serial, 0)