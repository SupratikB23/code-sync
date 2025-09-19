class Solution:
    def convertTemperature(self, Celsius: float) -> List[float]:
        L = [Celsius + 273.15, Celsius * 1.80 + 32.00]
        return L