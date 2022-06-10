from django.db import models
from django.urls import reverse


class BaseMetalA(models.Model):
    """Model representing a base metal A"""
    group_1 = 'Группы:1.1;1.2;11.1 СТБ ISO 15608 (Ст3,20,09Г2С,16ГС,17Г1С)'
    group_2 = 'Группа:6.2 CТБ ISO 15608 (12Х1МФ,15Х1М1Ф)'
    group_3 = 'Группа:8.1 CТБ ISO 15608 (12Х18Н9,12Х18Н9Т,12Х18Н12Т,08Н18Н10Т)'
    BASE_METAL_CHOISES = [
        (group_1, 'Группы:1.1;1.2;11.1 СТБ ISO 15608 (Ст3,20,09Г2С,16ГС,17Г1С)'),
        (group_2, 'Группа:6.2 CТБ ISO 15608 (12Х1МФ,15Х1М1Ф)'),
        (group_3, 'Группа:8.1 CТБ ISO 15608 (12Х18Н9,12Х18Н9Т,12Х18Н12Т,08Н18Н10Т)'),
    ]
    name = models.CharField(
        max_length=200,
        choices=BASE_METAL_CHOISES,
        help_text="Выберите основной металл А"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class BaseMetalB(models.Model):
    """Model representing a base metal B"""
    group_1 = 'Группы:1.1;1.2;11.1 СТБ ISO 15608 (Ст3,20,09Г2С,16ГС,17Г1С)'
    group_2 = 'Группа:6.2 CТБ ISO 15608 (12Х1МФ,15Х1М1Ф)'
    group_3 = 'Группа:8.1 CТБ ISO 15608 (12Х18Н9,12Х18Н9Т,12Х18Н12Т,08Н18Н10Т)'
    BASE_METAL_CHOISES = [
        (group_1, 'Группы:1.1;1.2;11.1 СТБ ISO 15608 (Ст3,20,09Г2С,16ГС,17Г1С)'),
        (group_2, 'Группа:6.2 CТБ ISO 15608 (12Х1МФ,15Х1М1Ф)'),
        (group_3, 'Группа:8.1 CТБ ISO 15608 (12Х18Н9,12Х18Н9Т,12Х18Н12Т,08Н18Н10Т)'),
    ]
    name = models.CharField(
        max_length=200,
        choices=BASE_METAL_CHOISES,
        help_text="Выберите основной металл B"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class WeldingProcess(models.Model):
    """Model representing a welding process"""
    process_111 = '111'
    process_135 = '135'
    process_141 = '141'
    process_111_141 = '111+141'
    WELD_PROCESS_CHOISES = [
        (process_111, 'Ручная дуговая сварка'),
        (process_135, 'Дуговая сварка в защитных газах'),
        (process_141, 'Сварка неплавящимся электродом'),
        (process_111_141, 'Ручная дуговая сварка неплавящимся электродом'),
    ]
    name = models.CharField(
        max_length=200,
        choices=WELD_PROCESS_CHOISES,
        help_text="Выберите процесс сварки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class WeldType(models.Model):
    """Model representing a weld type"""
    type_1 = 'BW'
    type_2 = 'FW'
    WELD_TYPE_CHOISES = [
        (type_1, 'Butt Weld'),
        (type_2, 'Fillet Weld'),
    ]
    name = models.CharField(
        max_length=10,
        choices=WELD_TYPE_CHOISES,
        help_text="Выберите тип сварного соединения"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Positions(models.Model):
    """Model representing a positions"""
    PA = 'PA'
    PB = 'PB'
    PC = 'PC'
    PD = 'PD'
    PE = 'PE'
    PF = 'PF'
    PG = 'PG'
    PH = 'PH'
    PJ = 'PJ'
    POSITION_CHOISES = [
        (PA, 'PA'),
        (PB, 'PB'),
        (PC, 'PC'),
        (PD, 'PD'),
        (PE, 'PE'),
        (PF, 'PF'),
        (PG, 'PG'),
        (PH, 'PH'),
        (PJ, 'PJ'),
    ]
    name = models.CharField(
        max_length=10,
        choices=POSITION_CHOISES,
        help_text="Выберите позиции"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class PartSize(models.Model):
    """Model representing a size of parts"""
    size = models.CharField(
        max_length=20,
        help_text="Укажите типоразмер деталей, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.size


class WeldConstruction(models.Model):
    """Model representing a weld construction"""
    name = models.ImageField(
        help_text="Выберите схему конструкции сварного соединения"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class SectionAngle(models.Model):
    """Model representing a section angle"""
    angle = models.CharField(
        max_length=20,
        help_text="Укажите угол разделки кромок"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.angle


class GapSize(models.Model):
    """Model representing a gap size"""
    gapsize = models.CharField(
        max_length=10,
        help_text="Укажите величину зазора в собранном стыке, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.gapsize


class EdgeBluntingSize(models.Model):
    """Model representing an edge blunting size"""
    edgesize = models.CharField(
        max_length=10,
        help_text="Укажите величину притупления кромок, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.edgesize


class WeldingSequence(models.Model):
    """Model representing a welding sequence"""
    name = models.ImageField(
        help_text="Выберите схему последовательности процесса сварки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class SeamWidth(models.Model):
    """Model representing a seam width"""
    seamwidth = models.CharField(
        max_length=5,
        help_text="Укажите ширину шва, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.seamwidth


class SeamReinforceHeight(models.Model):
    """Model representing a seam reinforce height"""
    height = models.CharField(
        max_length=5,
        help_text="Укажите высоту усиления шва, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.height


class ExcessPenetration(models.Model):
    """Model representing an excess penetration"""
    excess = models.CharField(
        max_length=5,
        help_text="Укажите превышение проплава на высоту, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.excess


class FillerType(models.Model):
    """Model representing a filler type"""
    FM1 = 'FM1'
    FM2 = 'FM2'
    FM3 = 'FM3'
    FM4 = 'FM4'
    FM5 = 'FM5'
    FM6 = 'FM6'
    FILLER_CHOISES = [
        (FM1, 'Non-alloy and fine grain steels'),
        (FM2, 'High-strength steels'),
        (FM3, 'Creep-resisting steels Cr < 3.75 %'),
        (FM4, 'Creep-resisting steels 3.75 <= Cr <= 12 %'),
        (FM5, 'Stainless and heat-resisting steels'),
        (FM6, 'Nickel and nickel alloys'),
    ]
    name = models.CharField(
        max_length=15,
        choices=FILLER_CHOISES,
        help_text="Выберите тип присадочного материала"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class FillerDiameter(models.Model):
    """Model representing an excess penetration"""
    diameter = models.CharField(
        max_length=5,
        help_text="Укажите диаметр присадочного материала, мм"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.diameter


class AmperageType(models.Model):
    """Model representing an amperage type"""
    AC = 'AC'
    DC_1 = 'DC+'
    DC_2 = 'DC-'
    pulsed = 'Pulsed'
    AMPERAGE_TYPE_CHOISES = [
        (AC, 'AC'),
        (DC_1, 'DC+'),
        (DC_2, 'DC-'),
        (pulsed, 'Pulsed'),
    ]
    type = models.CharField(
        max_length=10,
        choices=AMPERAGE_TYPE_CHOISES,
        help_text="Выберите род/полярность тока"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.type


class Amperage(models.Model):
    """Model representing an amperage"""
    amperage = models.CharField(
        max_length=10,
        help_text="Укажите силу тока, А"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.amperage


class Voltage(models.Model):
    """Model representing a voltage"""
    voltage = models.CharField(
        max_length=10,
        help_text="Укажите напряжение, В"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.voltage


class Speed(models.Model):
    """Model representing a welding speed"""
    speed = models.CharField(
        max_length=10,
        help_text="Укажите скорость, м/мин"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.speed


class Calcination(models.Model):
    """Model representing a caltination"""
    caltination = models.CharField(
        max_length=10,
        help_text="Укажите необходимость прокалки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.caltination


class HeatingTemp(models.Model):
    """Model representing a heating teperature"""
    temp = models.CharField(
        max_length=5,
        help_text="Укажите температуру подогрева"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.temp


class HeatingMethod(models.Model):
    """Model representing a heating method"""
    conv = 'Конвективный'
    ind = 'Индукционный'
    rad = 'Радиационный'
    HEATING_METHOD_CHOISES = [
        (conv, 'Конвективный'),
        (ind, 'Индукционный'),
        (rad, 'Радиационный'),
    ]
    name = models.CharField(
        max_length=20,
        choices=HEATING_METHOD_CHOISES,
        help_text="Укажите необходимость прокалки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class KeepingHeating(models.Model):
    """Model representing a keeping heating"""
    keep_1 = 'Да'
    keep_2 = 'Нет'
    KEEPING_HEATING_CHOISES = [
        (keep_1, 'Да'),
        (keep_2, 'Нет'),
    ]
    name = models.CharField(
        max_length=5,
        choices=KEEPING_HEATING_CHOISES,
        help_text="Укажите необходимость поддержания подогрева"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class InterRollerTemp(models.Model):
    """Model representing an interroller teperature"""
    temp = models.CharField(
        max_length=10,
        help_text="Укажите межваликовую температуру"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.temp


class HeatTreatType(models.Model):
    """Model representing a heat treating type"""
    name = models.CharField(
        max_length=20,
        help_text="Укажите вид термической обработки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class TempRiseSpeed(models.Model):
    """Model representing a teperature rise speed"""
    speed = models.CharField(
        max_length=20,
        help_text="Укажите скорость подъема температуры"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.speed


class Temperature(models.Model):
    """Model representing an afterwelding teperature"""
    temp = models.CharField(
        max_length=10,
        help_text="Укажите температуру"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.temp


class HoldingTime(models.Model):
    """Model representing a holding time"""
    time = models.CharField(
        max_length=20,
        help_text="Укажите время выдержки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.time


class CoolingSpeed(models.Model):
    """Model representing a cooling speed"""
    speed = models.CharField(
        max_length=20,
        help_text="Укажите скорость охлаждения"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.speed


class ShieldingGas(models.Model):
    """Model representing a type of shielding gas"""
    name = models.CharField(
        max_length=10,
        help_text="Укажите тип защитного газа"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class RootProtection(models.Model):
    """Model representing a root protection"""
    root_1 = 'Да'
    root_2 = 'Нет'
    ROOT_PROTECTION_CHOISES = [
        (root_1, 'Да'),
        (root_2, 'Нет'),
    ]
    protection = models.CharField(
        max_length=5,
        choices=ROOT_PROTECTION_CHOISES,
        help_text="Укажите необходимость защиты корня"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.protection


class GasConsumption(models.Model):
    """Model representing a gas consumption"""
    consump = models.CharField(
        max_length=20,
        help_text="Укажите расход защитного газа"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.consump


class TungstenElectrode(models.Model):
    """Model representing a type of electrode"""
    wp = 'WP'
    wt = 'WT-20'
    wc = 'WC-20'
    wl1 = 'WL-15'
    wl2 = 'WL-20'
    wy = 'WY-20'
    wz = 'WZ-8'
    ELECTRODE_CHOISES = [
        (wp, 'WP'),
        (wt, 'WT-20'),
        (wc, 'WC-20'),
        (wl1, 'WL-15'),
        (wl2, 'WL-20'),
        (wy, 'WY-20'),
        (wz, 'WZ-8'),
    ]
    electrode = models.CharField(
        max_length=10,
        choices=ELECTRODE_CHOISES,
        help_text="Укажите тип вольфрамового электрода"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.electrode


class TransverseVibrations(models.Model):
    """Model representing a transverse vibrations"""
    vibr_1 = 'Да'
    vibr_2 = 'Нет'
    VIBRATION_CHOISES = [
        (vibr_1, 'Да'),
        (vibr_2, 'Нет'),
    ]
    vibration = models.CharField(
        max_length=5,
        choices=VIBRATION_CHOISES,
        help_text="Укажите необходимость поперечных колебаний"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.vibration


class EdgePrepapration(models.Model):
    """Model representing an edge prepapration"""
    edge_1 = 'Ручная'
    edge_2 = 'Механическая'
    EDGE_PREPAPRATION_CHOISES = [
        (edge_1, 'Ручная'),
        (edge_2, 'Механическая'),
    ]
    preparation = models.CharField(
        max_length=15,
        choices=EDGE_PREPAPRATION_CHOISES,
        help_text="Укажите вид подготовки свариваемых кромок"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.preparation


class PulseWelding(models.Model):
    """Model representing a pulse welding"""
    pulse_1 = 'Да'
    pulse_2 = 'Нет'
    PULSE_CHOISES = [
        (pulse_1, 'Да'),
        (pulse_2, 'Нет'),
    ]
    pulse = models.CharField(
        max_length=5,
        choices=PULSE_CHOISES,
        help_text="Укажите необходимость применения импульсной сварки"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.pulse


class RollerCleaning(models.Model):
    """Model representing a roller cleaning"""
    clean_1 = 'Ручная'
    clean_2 = 'Механическая'
    CLEANING_CHOISES = [
        (clean_1, 'Ручная'),
        (clean_2, 'Механическая'),
    ]
    cleaning = models.CharField(
        max_length=15,
        choices=CLEANING_CHOISES,
        help_text="Укажите тип зачистки валиков"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.cleaning


class WPS(models.Model):
    """Model representing a WPS-instuction"""
    number = models.CharField(max_length=10)
    base_metal_A = models.ForeignKey(BaseMetalA, on_delete=models.SET_NULL, null=True)
    base_metal_B = models.ForeignKey(BaseMetalB, on_delete=models.SET_NULL, null=True)
    welding_process = models.ForeignKey(WeldingProcess, on_delete=models.SET_NULL, null=True)
    weld_type = models.ForeignKey(WeldType, on_delete=models.SET_NULL, null=True)
    positions = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True)
    part_size = models.ForeignKey(PartSize, on_delete=models.SET_NULL, null=True)
    weld_construction = models.ForeignKey(WeldConstruction, on_delete=models.SET_NULL, null=True)
    section_angle = models.ForeignKey(SectionAngle, on_delete=models.SET_NULL, null=True)
    gap_size = models.ForeignKey(GapSize, on_delete=models.SET_NULL, null=True)
    edge_blunting_size = models.ForeignKey(EdgeBluntingSize, on_delete=models.SET_NULL, null=True)
    welding_sequence = models.ForeignKey(WeldingSequence, on_delete=models.SET_NULL, null=True)
    seam_width = models.ForeignKey(SeamWidth, on_delete=models.SET_NULL, null=True)
    seam_reinforce_height = models.ForeignKey(SeamReinforceHeight, on_delete=models.SET_NULL, null=True)
    excess_penetration = models.ForeignKey(ExcessPenetration, on_delete=models.SET_NULL, null=True)
    filler_type = models.ForeignKey(FillerType, on_delete=models.SET_NULL, null=True)
    filler_diameter = models.ForeignKey(FillerDiameter, on_delete=models.SET_NULL, null=True)
    amperage_type = models.ForeignKey(AmperageType, on_delete=models.SET_NULL, null=True)
    amperage = models.ForeignKey(Amperage, on_delete=models.SET_NULL, null=True)
    voltage = models.ForeignKey(Voltage, on_delete=models.SET_NULL, null=True)
    speed = models.ForeignKey(Speed, on_delete=models.SET_NULL, null=True)
    calcination = models.ForeignKey(Calcination, on_delete=models.SET_NULL, null=True)
    heating_temp = models.ForeignKey(HeatingTemp, on_delete=models.SET_NULL, null=True)
    heating_method = models.ForeignKey(HeatingMethod, on_delete=models.SET_NULL, null=True)
    keeping_heating = models.ForeignKey(KeepingHeating, on_delete=models.SET_NULL, null=True)
    inter_roller_temp = models.ForeignKey(InterRollerTemp, on_delete=models.SET_NULL, null=True)
    heat_treat_type = models.ForeignKey(HeatTreatType, on_delete=models.SET_NULL, null=True)
    temp_rise_speed = models.ForeignKey(TempRiseSpeed, on_delete=models.SET_NULL, null=True)
    temperature = models.ForeignKey(Temperature, on_delete=models.SET_NULL, null=True)
    holding_time = models.ForeignKey(HoldingTime, on_delete=models.SET_NULL, null=True)
    cooling_speed = models.ForeignKey(CoolingSpeed, on_delete=models.SET_NULL, null=True)
    shielding_gas = models.ForeignKey(ShieldingGas, on_delete=models.SET_NULL, null=True)
    root_protection = models.ForeignKey(RootProtection, on_delete=models.SET_NULL, null=True)
    gas_consumption = models.ForeignKey(GasConsumption, on_delete=models.SET_NULL, null=True)
    tungsten_electrode = models.ForeignKey(TungstenElectrode, on_delete=models.SET_NULL, null=True)
    transverse_vibrations = models.ForeignKey(TransverseVibrations, on_delete=models.SET_NULL, null=True)
    edge_preparation = models.ForeignKey(EdgePrepapration, on_delete=models.SET_NULL, null=True)
    pulse_welding = models.ForeignKey(PulseWelding, on_delete=models.SET_NULL, null=True)
    roller_cleaning = models.ForeignKey(RollerCleaning, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.number)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('WPS-detail', args=[str(self.number)])
