from decimal import Decimal


class ConversionTool:
    def __init__(self):
        self.conversion_factors = {
            "Millimeter (mm)": Decimal("0.001"),
            "Centimeter (cm)": Decimal("0.01"),
            "Decimeter (dm)": Decimal("0.1"),
            "Meter (m)": Decimal("1.0"),
            "Decameter (dam)": Decimal("10.0"),
            "Hectometer (hm)": Decimal("100.0"),
            "Kilometer (km)": Decimal("1000.0"),
            "Inch (in)": Decimal("0.0254"),
            "Foot (ft)": Decimal("0.3048"),
            "Yard (yd)": Decimal("0.9144"),
            "Mile (mi)": Decimal("1609.34")
        }

    def calculating(self, number, local_input_unit, local_output_unit):
        input_factor = self.conversion_factors[local_input_unit]
        output_factor = self.conversion_factors[local_output_unit]

        local_result = Decimal(str(number)) * (input_factor / output_factor)

        if local_result >= Decimal("10000") or local_result <= Decimal("0.0001"):
            local_result = local_result.normalize()
        else:
            local_result = float(local_result)

        if local_result % 1 == 0:
            return "{:.1f}".format(local_result)
        else:
            return "{:.4f}".format(local_result)
