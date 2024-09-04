'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
class CuentaBancaria:

  def mostrar_menu():
    print("\ln--- !Bienvenido al Banco! ---\ln")
    print("\n--- Menú de Cuentas Bancarias ---")
    print("1. Abrir una nueva cuenta")
    print("2. Realizar una consignación")
    print("3. Realizar un retiro")
    print("4. Mostrar información de la cuenta")
    print("5. Salir")

  def main():
    while True:
        mostrar_menu()
        opciones = int(input(¿Que deseas hacer?))
        if opciones == 1:
            Abrirnuevacuenta()
        if opciones == 2:
            Realizarconsignacion()
        if opciones == 3:
            Realizarunretiro()
        if opciones == 4:
            Mostrarinformacion()
        if opciones == 5:
            Salir()
            
            
            

if __name__ == "__main__":
    main()
