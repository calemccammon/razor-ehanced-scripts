from System.Collections.Generic import List
from System import Byte

def targetClosestEnemy():
    filter = Mobiles.Filter()
    filter.CheckIgnoreObject = True
    filter.Enabled = True
    filter.RangeMin = 0
    filter.RangeMax = 10
    filter.Notorieties = List[Byte](bytes([3,4,5,6]))
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies,'Nearest')
    return enemy

enemy = targetClosestEnemy()

if enemy and enemy.Name != 'an energy vortex' and enemy.Name != 'a blade spirit' and enemy.Name != 'a rising colossus' and enemy.Name != 'a patchwork skeleton':
    Target.SetLast(enemy)
    if Player.GetSkillValue('Bushido') >= 50.0 and enemy.Hits == enemy.HitsMax:
        Player.InvokeVirtue('Honor')
        Target.WaitForTarget(3000)
        Target.Last()
    Player.Attack(enemy)