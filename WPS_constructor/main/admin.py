from django.contrib import admin
from .models import BaseMetalA, BaseMetalB, WeldingProcess, WeldType, Positions, PartSize, WeldConstruction, \
    SectionAngle, GapSize, EdgeBluntingSize, WeldingSequence, SeamWidth, SeamReinforceHeight, ExcessPenetration, \
    FillerType, FillerDiameter, AmperageType, Amperage, Voltage, Speed, Calcination, HeatingTemp, HeatingMethod, \
    KeepingHeating, InterRollerTemp, HeatTreatType, TempRiseSpeed, Temperature, HoldingTime, CoolingSpeed, \
    ShieldingGas, RootProtection, GasConsumption, TungstenElectrode, TransverseVibrations, EdgePrepapration, \
    PulseWelding, RollerCleaning, WPS


admin.site.register(BaseMetalA)
admin.site.register(BaseMetalB)
admin.site.register(WeldingProcess)
admin.site.register(WeldType)
admin.site.register(Positions)
admin.site.register(PartSize)
admin.site.register(WeldConstruction)
admin.site.register(SectionAngle)
admin.site.register(GapSize)
admin.site.register(EdgeBluntingSize)
admin.site.register(WeldingSequence)
admin.site.register(SeamWidth)
admin.site.register(SeamReinforceHeight)
admin.site.register(ExcessPenetration)
admin.site.register(FillerType)
admin.site.register(FillerDiameter)
admin.site.register(AmperageType)
admin.site.register(Amperage)
admin.site.register(Voltage)
admin.site.register(Speed)
admin.site.register(Calcination)
admin.site.register(HeatingTemp)
admin.site.register(HeatingMethod)
admin.site.register(KeepingHeating)
admin.site.register(InterRollerTemp)
admin.site.register(HeatTreatType)
admin.site.register(TempRiseSpeed)
admin.site.register(Temperature)
admin.site.register(HoldingTime)
admin.site.register(CoolingSpeed)
admin.site.register(ShieldingGas)
admin.site.register(RootProtection)
admin.site.register(GasConsumption)
admin.site.register(TungstenElectrode)
admin.site.register(TransverseVibrations)
admin.site.register(EdgePrepapration)
admin.site.register(PulseWelding)
admin.site.register(RollerCleaning)
admin.site.register(WPS)
