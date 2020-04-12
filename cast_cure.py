if Player.Poisoned and not Player.Paralized:
    Spells.CastMagery('Cure')
    Target.WaitForTarget(15000)
    Target.Self()