from itv import *

def test_lee_inspecciones(datos:List[ITV])->None:
    print("\n"+"test_lee_inspecciones")
    print("Número de registros leídos:", len(datos))
    print(f"Los dos primeros {datos[:2]}")
    print(f"Los dos últimos {datos[-2:]}")

def test_inspecciones_entre_fechas(datos:List[ITV])->None:
    print("\ntest_inspecciones_entre_fechas")
    f1 = date(2024,9,20)
    print(f"Las inspecciones realizadas después de {f1} son: {inspecciones_entre_fechas(datos,f1=f1)}")
    f2 = date(2019,1,15)
    print(f"Las inspecciones realizadas antes de {f2} son: {inspecciones_entre_fechas(datos,f2=f2)}")
    f1 = date(2022,3,25)
    f2 = date(2022,5,20)
    print(f"Las inspecciones realizadas entre {f1} y {f2} son: {inspecciones_entre_fechas(datos,f1=f1,f2=f2)}")

def test_promedio_de_días_de_adelanto(datos:List[ITV])->None:
    print("\ntest_promedio_de_días_de_adelanto")
    valor_inspección = "fav"
    print(f"El promedio de dias de todas la estaciones con resultado {valor_inspección} es: {promedio_de_días_de_adelanto(datos,valor_inspección)}")
    valor_inspección = "des"
    estación = "Sevilla-Gelves"
    print(f"El promedio de dias con resultado {valor_inspección} de la estación {estación} es: {promedio_de_días_de_adelanto(datos,valor_inspección,"Sevilla-Gelves")}")
    valor_inspección = "fav"
    print(f"El promedio de dias con resultado {valor_inspección} de la estación {estación} es: {promedio_de_días_de_adelanto(datos,valor_inspección,"Sevilla-Gelves")}")
    valor_inspección = "fav"
    estación = "New York"
    print(f"el promedio de dias con resultado {valor_inspección} de la estación {estación} es: {promedio_de_días_de_adelanto(datos,"fav","New York")}")

def test_importes_comunes(datos:List[ITV])->None:
    print("\ntest_importes_comunes")
    estación1 = "Sevilla-Gelves"
    estación2 = "Sevilla-El Pino"
    comunes = importes_comunes(datos,estación1,estación2)
    print(f"Los importes comunes a {estación1} y a {estación2} son: {comunes}")
    estación1 = "La Rinconada"
    estación2 = "Utrera"
    comunes = importes_comunes(datos,estación1,estación2)
    print(f"\nLos importes comunes a {estación1} y a {estación2} son: {comunes}")

def test_diferencia_entre_importes(datos:List[ITV])->None:
    print("\ntest_diferencia_entre_importes")
    diferencias = diferencia_entre_importes(datos)
    for indice,tupla in enumerate(diferencias):
        print(f"{indice+1}. La diferencia entre {tupla[0]} y {tupla[1]} es {tupla[2]}")

if __name__ == "__main__":
    ITVs = lee_inspecciones("ProgramasPython\T09_ITV_extendido2\data\inspecciones.csv")
    test_lee_inspecciones(ITVs)
    test_inspecciones_entre_fechas(ITVs)
    test_promedio_de_días_de_adelanto(ITVs)
    test_importes_comunes(ITVs)
    test_diferencia_entre_importes(ITVs)