if Player.Poisoned:
    Spells.CastChivalry('Cleanse By Fire')
    Target.WaitForTarget(5000)
    Target.Self()