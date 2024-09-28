def Salario():
    Horas_laboradas = float(input("Ingrese la cantidad de horas laboradas en la semana:"))
    Tarifas_x_hora = float(input("Ingrese su tarifa por hora laboral:"))
    Años_Antiguedad = float(input("Ingrese su tiempo de antiguedad:"))
    Ventas_realizadas = float(input("Ingrese la cantidad de ventas realizadas (solo si aplica):"))

    if Horas_laboradas > 40:
        Horas_normales = 40
        Horas_extras = Horas_laboradas - 40
        Salario_base = (Horas_normales * Tarifas_x_hora) + (Horas_extras * Tarifas_x_hora * 1.5)
    else:
        Salario_base = Horas_laboradas * Tarifas_x_hora

    Bono_Antiguedad = 0
    if Años_Antiguedad >= 5:
        Bono_Antiguedad = Salario_base * 0.05

    Comision = 0
    if Ventas_realizadas > 1000:
        Comision = (Ventas_realizadas - 1000) * 0.02

    Salario_sin_desc = Salario_base + Años_Antiguedad + Comision

    if Salario_sin_desc <= 1000:
        Desc = Salario_sin_desc * 0.10
    elif Salario_sin_desc <= 2000:
        Desc = 0.10 + (Salario_sin_desc - 1000) * 0.05
    else:
        Desc = 100 + 50 + (Salario_sin_desc - 2000) * 0.03

    Salario_final = Salario_sin_desc - Desc

    print("Resumen Salario:")
    print(f"Salario Base: ${Salario_base}")
    print(f"Bono Antiguedad: ${Bono_Antiguedad}")
    print(f"Comision: {Comision}")
    print(f"Salario Bruto: {Salario_sin_desc}")
    print(f"Descuento: {Desc}")
    print(f"Salario Neto: {Salario_final}")

Salario()