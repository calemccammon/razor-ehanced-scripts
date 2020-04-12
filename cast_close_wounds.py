if Player.Hits < Player.HitsMax and not Player.Poisoned:
    Spells.CastChivalry('Close Wounds')
    Target.WaitForTarget(5000)
    Target.Self()