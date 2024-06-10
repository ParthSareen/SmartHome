from dataclasses import dataclass
@dataclass
class SensorData:
    operating_status: int
    air_quality_index: int
    tvoc_ppb: int  # Total Volatile Organic Compounds in parts per billion
    eco2_ppm: int  # Equivalent CO2 concentration in parts per million
    temperature_celsius: float
    pressure_pa: int
    altitude_meter: float
    humidity_percent: float
