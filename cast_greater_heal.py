if not Player.Poisoned and not Player.Paralized:
    Spells.CastMagery('Greater Heal')
    Target.WaitForTarget(15000)
    Target.Self()