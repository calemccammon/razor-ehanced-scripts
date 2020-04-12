def getLegendaries():
    filter = Items.Filter()
    filter.CheckIgnoreObject = True
    filter.Enabled = True
    filter.IsCorpse = 0
    filter.Movable = True
    return Items.ApplyFilter(filter)
    
def lootLegendaries():
    items = getLegendaries()
    for item in items:
        Player.ChatSay(0, str(Items.FindBySerial(item.Container).Name))
        if 'Legendary Artifact' in str(Items.GetPropStringList(item)):
            Player.ChatSay(0, 'test2')
            
lootLegendaries()