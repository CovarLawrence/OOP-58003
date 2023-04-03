def main():

    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = int(input("Enter the temperature in Celsius: "))
    tempInKelvin = int(input("Enter the temperature in Kelvin: "))
    tempInFahrenheit = int(input("Enter the temperature in Fahrenheit: "))

    convert = CelsiusToKelvin(tempInCelsius)
    print(int(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(int(convert.conversion()) + " Fahrenheit")
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(int(convert.conversion()) + " Celsius")
    convert = KelvinToCelsius(tempInKelvin)
    print(int(convert.conversion()) + " Celsius")

if __name__ == '__main__':
    main()
