'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
import datetime

class CuentaBancaria:
    def __init__(self, numeroCta=None, nombreCliente=None, fechaApertura=None, saldo=0.0):
        if numeroCta and nombreCliente and fechaApertura:
            self.__numeroCta = numeroCta
            self.__nombreCliente = nombreCliente
            self.__fechaApertura = fechaApertura
            self.__saldo = saldo
        else:
            self.__numeroCta = ""
            self.__nombreCliente = ""
            self.__fechaApertura = ""
            self.__saldo = 0.0

    def getNumeroCta(self):
        return self.__numeroCta

    def getNombreCliente(self):
        return self.__nombreCliente

    def getFechaApertura(self):
        return self.__fechaApertura

    def getSaldo(self):
        return self.__saldo

    def setNumeroCta(self, numeroCta):
        self.__numeroCta = numeroCta

    def setNombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def setFechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def abrir_cuenta(self, numeroCta, nombreCliente, saldoInicial):
        if saldoInicial < 100000:
            print("La suma de dinero inicial debe ser mayor a 100000 pesos")
            return False
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldo = saldoInicial
        self.__fechaApertura = datetime.date.today()
        print("Registro de nuevo cliente exitoso")
        return True

    def realizar_consignacion(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a consignar debe ser positiva")

    def realizar_retiro(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad inválida para retiro")

    def mostrar_informacion(self):
        print(f"Número de cuenta: {self.__numeroCta}")
        print(f"Nombre del cliente: {self.__nombreCliente}")
        print(f"Fecha de apertura: {self.__fechaApertura}")
        print(f"Saldo actual: {self.__saldo}")

def mostrar_menu():
    print("\n --- !Bienvenido al Banco! ---")
    print("\n -- Menú de Cuentas Bancarias --\n")
    print("1. Abrir una nueva cuenta")
    print("2. Realizar una consignación")
    print("3. Realizar un retiro")
    print("4. Mostrar información de la cuenta")
    print("5. Salir")

def main():
    cuentas = {}
    cuenta_actual = None
    
    while True:
        mostrar_menu()
        opcion = int(input("¿Qué deseas hacer? "))
        
        if opcion == 1:
            numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                print("Error: Ya existe una cuenta con ese número.")
                continue
            nombreCliente = input("Ingrese el nombre del cliente: ")
            saldoInicial = float(input("Ingrese el saldo inicial (mínimo 100,000 pesos): "))
            nueva_cuenta = CuentaBancaria()
            if nueva_cuenta.abrir_cuenta(numeroCta, nombreCliente, saldoInicial):
                cuentas[numeroCta] = nueva_cuenta
                cuenta_actual = nueva_cuenta
        elif opcion == 2:
            if cuenta_actual:
                cantidad = float(input("Ingrese la cantidad a consignar: "))
                cuenta_actual.realizar_consignacion(cantidad)
            else:
                print("Primero debes abrir una cuenta")
        elif opcion == 3:
            if cuenta_actual:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta_actual.realizar_retiro(cantidad)
            else:
                print("Primero debes abrir una cuenta")
        elif opcion == 4:
            if cuenta_actual:
                cuenta_actual.mostrar_informacion()
            else:
                print("Primero debes abrir una cuenta")
        elif opcion == 5:
            print("Adiós")
            break
        else:
            print("Opción inválida. Selecciona una opción válida del menú")
            
if __name__ == "__main__":
    main()

