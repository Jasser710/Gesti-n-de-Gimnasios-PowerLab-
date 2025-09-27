from clases.ClaseGrupal import ClaseGrupal
from clases.Cliente import Cliente
from clases.Instructor import Instructor
from clases.Medicion import Medicion
from clases.Rutina import Rutina
from clases.Sucursal import Sucursal

# Almacenamiento global
sucursales = []
instructores = []
clientes = []
clases_grupales = []

# Constantes
ESPECIALIDADES = ["CrossFit", "HIIT", "TRX", "Pesas", "Spinning", "Cardio", "Yoga", "Zumba"]
AREAS_CUERPO = ["Pecho y tríceps", "Bíceps", "Piernas", "Espalda"]

# ==================== FUNCIONES DE MENÚ ====================
def mostrar_menu_principal():
    print("\n" + "="*50)
    print("       SISTEMA POWERLAB - MENÚ PRINCIPAL")
    print("="*50)
    print("1. Gestión de Sucursales")
    print("2. Gestión de Instructores") 
    print("3. Gestión de Clientes")
    print("4. Registro de Mediciones")
    print("5. Gestión de Clases Grupales")
    print("6. Generar Rutinas")
    print("7. Salir")
    return input("Seleccione una opción (1-7): ")

# ==================== OPCIÓN 1: GESTIÓN DE SUCURSALES ====================
def gestionar_sucursales():
    while True:
        print("\n--- Gestión de Sucursales ---")
        print("1. Agregar Sucursal")
        print("2. Listar Sucursales")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_sucursal()
        elif opcion == "2":
            listar_sucursales()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")

def agregar_sucursal():
    if len(sucursales) >= 30:
        print("❌ Límite máximo de 30 sucursales alcanzado")
        return
    
    print("\n--- Agregar Nueva Sucursal ---")
    codigo = input("Código: ")
    provincia = input("Provincia: ")
    canton = input("Cantón: ")
    email = input("email: ")
    telefono = input("Teléfono: ")
    
    # Verificar si el código ya existe
    for sucursal in sucursales:
        if sucursal.codigo == codigo:
            print("❌ Ya existe una sucursal con ese código")
            return
    
    nueva_sucursal = Sucursal(codigo, provincia, canton, email, telefono)
    sucursales.append(nueva_sucursal)
    print("✅ Sucursal agregada exitosamente")

def listar_sucursales():
    if not sucursales:
        print("No hay sucursales registradas")
        return
    
    print("\n--- Sucursales Registradas ---")
    for i, sucursal in enumerate(sucursales, 1):
        print(f"{i}. Código: {sucursal.codigo} | {sucursal.canton}, {sucursal.provincia}")
        print(f"   Tel: {sucursal.telefono} | email: {sucursal.email}")
        print(f"   Instructores: {len(sucursal.instructores)} | Clientes: {len(sucursal.clientes)}")
        print()

# ==================== OPCIÓN 2: GESTIÓN DE INSTRUCTORES ====================
def gestionar_instructores():
    while True:
        print("\n--- Gestión de Instructores ---")
        print("1. Agregar Instructor")
        print("2. Listar Instructores")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_instructor()
        elif opcion == "2":
            listar_instructores()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")

def agregar_instructor():
    if not sucursales:
        print("❌ Primero debe crear una sucursal")
        return
    
    print("\n--- Agregar Nuevo Instructor ---")
    print("Seleccione la sucursal:")
    listar_sucursales()
    
    try:
        sucursal_idx = int(input("Número de sucursal: ")) - 1
        sucursal_seleccionada = sucursales[sucursal_idx]
        
        cedula = input("Cédula: ")
        nombre = input("Nombre completo: ")
        telefono = input("Teléfono: ")
        email = input("email: ")
        fecha_nacimiento = input("Fecha nacimiento (DD/MM/AAAA): ")
        
        # Verificar si la cédula ya existe
        for instructor in instructores:
            if instructor.cedula == cedula:
                print("❌ Ya existe un instructor con esa cédula")
                return
        
        # Selección de especialidades
        print("\nEspecialidades disponibles:")
        for i, esp in enumerate(ESPECIALIDADES, 1):
            print(f"{i}. {esp}")
        
        especialidades = []
        while True:
            try:
                opcion_esp = input("Seleccione especialidad (número) o 'fin' para terminar: ")
                if opcion_esp.lower() == 'fin':
                    break
                opcion_esp = int(opcion_esp) - 1
                if 0 <= opcion_esp < len(ESPECIALIDADES):
                    especialidad = ESPECIALIDADES[opcion_esp]
                    if especialidad not in especialidades:
                        especialidades.append(especialidad)
                        print(f"✅ Especialidad agregada: {especialidad}")
                    else:
                        print("❌ Especialidad ya agregada")
                else:
                    print("❌ Número inválido")
            except ValueError:
                print("❌ Ingrese un número válido")
        
        if not especialidades:
            print("❌ El instructor debe tener al menos una especialidad")
            return
        
        nuevo_instructor = Instructor(cedula, nombre, telefono, email, fecha_nacimiento, especialidades, sucursal_seleccionada)
        instructores.append(nuevo_instructor)
        sucursal_seleccionada.instructores.append(nuevo_instructor)
        print("✅ Instructor agregado exitosamente")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

def listar_instructores():
    if not instructores:
        print("No hay instructores registrados")
        return
    
    print("\n--- Instructores Registrados ---")
    for i, instructor in enumerate(instructores, 1):
        print(f"{i}. {instructor}")
        print(f"   Tel: {instructor.telefono} | Email: {instructor.email}")
        print()

# ==================== OPCIÓN 3: GESTIÓN DE CLIENTES ====================
def gestionar_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Asignar Instructor a Cliente")
        print("4. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            asignar_instructor_cliente()
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")

def agregar_cliente():
    if not sucursales:
        print("❌ Primero debe crear una sucursal")
        return
    
    print("\n--- Agregar Nuevo Cliente ---")
    print("Seleccione la sucursal:")
    listar_sucursales()
    
    try:
        sucursal_idx = int(input("Número de sucursal: ")) - 1
        sucursal_seleccionada = sucursales[sucursal_idx]
        
        cedula = input("Cédula: ")
        # Verificar si la cédula ya existe
        for cliente in clientes:
            if cliente.cedula == cedula:
                print("❌ Ya existe un cliente con esa cédula")
                return
        
        nombre = input("Nombre completo: ")
        telefono = input("Teléfono: ")
        email = input("email: ")
        fecha_nacimiento = input("Fecha nacimiento (DD/MM/AAAA): ")
        sexo = input("Sexo (M/F): ").upper()
        fecha_inscripcion = input("Fecha de inscripción (DD/MM/AAAA): ")
        
        nuevo_cliente = Cliente(cedula, nombre, telefono, email, fecha_nacimiento, sexo, fecha_inscripcion, sucursal_seleccionada)
        clientes.append(nuevo_cliente)
        sucursal_seleccionada.clientes.append(nuevo_cliente)
        print("✅ Cliente agregado exitosamente")
        
        # Preguntar si asignar instructor ahora
        if sucursal_seleccionada.instructores:
            asignar_ahora = input("¿Desea asignar un instructor ahora? (s/n): ").lower()
            if asignar_ahora == 's':
                asignar_instructor_a_cliente(nuevo_cliente, sucursal_seleccionada)
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

def listar_clientes():
    if not clientes:
        print("No hay clientes registrados")
        return
    
    print("\n--- Clientes Registrados ---")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente}")  # ✅ Esto ahora mostrará sucursal e instructor automáticamente
        print(f"   Mediciones: {len(cliente.mediciones)}/10 | Clases: {len(cliente.clases_inscritas)}/3")
        print()

def asignar_instructor_cliente():
    if not clientes:
        print("❌ No hay clientes registrados")
        return
    
    print("Seleccione el cliente:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        # Encontrar la sucursal del cliente
        sucursal_cliente = None
        for sucursal in sucursales:
            if cliente_seleccionado in sucursal.clientes:
                sucursal_cliente = sucursal
                break
        
        if not sucursal_cliente or not sucursal_cliente.instructores:
            print("❌ No hay instructores disponibles en la sucursal del cliente")
            return
        
        asignar_instructor_a_cliente(cliente_seleccionado, sucursal_cliente)
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

def asignar_instructor_a_cliente(cliente, sucursal):
    print(f"\nInstructores disponibles en {sucursal.canton}:")
    for i, instructor in enumerate(sucursal.instructores, 1):
        print(f"{i}. {instructor.nombre} - {', '.join(instructor.especialidades)}")
    
    try:
        instructor_idx = int(input("Seleccione instructor: ")) - 1
        instructor_seleccionado = sucursal.instructores[instructor_idx]
        cliente.instructor_asignado = instructor_seleccionado
        print(f"✅ Instructor {instructor_seleccionado.nombre} asignado a {cliente.nombre}")
    except (ValueError, IndexError):
        print("❌ Selección inválida")

# ==================== OPCIÓN 4: REGISTRO DE MEDICIONES ====================
def gestionar_mediciones():
    while True:
        print("\n--- Registro de Mediciones ---")
        print("1. Nueva Medición")
        print("2. Ver Historial de Mediciones")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            nueva_medicion()
        elif opcion == "2":
            ver_historial_mediciones()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")

def nueva_medicion():
    if not clientes:
        print("❌ No hay clientes registrados")
        return
    
    print("Seleccione el cliente para la medición:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        # Verificar máximo de mediciones
        if len(cliente_seleccionado.mediciones) >= 10:
            print("❌ Límite máximo de 10 mediciones alcanzado para este cliente")
            return
        
        # Verificar que tenga instructor asignado
        if not cliente_seleccionado.instructor_asignado:
            print("❌ El cliente no tiene instructor asignado")
            return
        
        print(f"\n--- Nueva Medición para {cliente_seleccionado.nombre} ---")
        fecha = input("Fecha de medición (DD/MM/AAAA): ")
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
        porcentaje_grasa = float(input("Porcentaje de grasa (%): "))
        porcentaje_musculo = float(input("Porcentaje de músculo (%): "))
        edad_metabolica = int(input("Edad metabólica: "))
        grasa_visceral = float(input("Grasa visceral (%): "))
        cintura = float(input("Medida de cintura (cm): "))
        cadera = float(input("Medida de cadera (cm): "))
        pecho = float(input("Medida de pecho (cm): "))
        muslo = float(input("Medida de muslo (cm): "))
        
        # Cálculos automáticos
        imc = peso / (estatura ** 2)
        
        # Clasificación IMC
        if imc < 16.00:
            clasificacion = "Delgadez severa"
        elif imc <= 16.99:
            clasificacion = "Delgadez moderada"
        elif imc <= 18.49:
            clasificacion = "Delgadez leve"
        elif imc <= 24.99:
            clasificacion = "Normal"
        elif imc <= 29.99:
            clasificacion = "Pre-obesidad"
        elif imc <= 34.99:
            clasificacion = "Obesidad leve"
        elif imc <= 39.99:
            clasificacion = "Obesidad media"
        else:
            clasificacion = "Obesidad mórbida"
        
        # Cálculo de proteína
        base_proteina = peso * 0.8
        if cliente_seleccionado.sexo == 'M':
            proteina_recomendada = base_proteina * 2.1  # Hombres activos
        else:
            proteina_recomendada = base_proteina * 1.7  # Mujeres activas
        
        # Cálculo de agua
        vasos_agua = peso / 7
        
        # Crear medición
        nueva_medicion = Medicion(
            fecha, peso, estatura, porcentaje_grasa, porcentaje_musculo,
            edad_metabolica, grasa_visceral, cintura, cadera, pecho, muslo,
            imc, clasificacion, proteina_recomendada, vasos_agua
        )
        
        cliente_seleccionado.mediciones.append(nueva_medicion)
        
        # Mostrar reporte
        print("\n" + "="*50)
        print("          REPORTE DE MEDICIÓN")
        print("="*50)
        print(f"Cliente: {cliente_seleccionado.nombre}")
        print(f"Fecha: {fecha}")
        print(f"IMC: {imc:.2f} - Clasificación: {clasificacion}")
        print(f"Proteína diaria recomendada: {proteina_recomendada:.1f}g")
        print(f"Vasos de agua recomendados: {vasos_agua:.1f} vasos de 250ml")
        if clasificacion in ["Obesidad leve", "Obesidad media", "Obesidad mórbida"]:
            print("⚠️  CLIENTE DE ALTO RIESGO")
        print("="*50)
        
    except (ValueError, IndexError):
        print("❌ Datos inválidos")

def ver_historial_mediciones():
    if not clientes:
        print("❌ No hay clientes registrados")
        return
    
    print("Seleccione el cliente:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        if not cliente_seleccionado.mediciones:
            print("❌ El cliente no tiene mediciones registradas")
            return
        
        print(f"\n--- Historial de Mediciones de {cliente_seleccionado.nombre} ---")
        for i, medicion in enumerate(cliente_seleccionado.mediciones, 1):
            print(f"\nMedición #{i} - Fecha: {medicion.fecha}")
            print(f"  Peso: {medicion.peso}kg | Estatura: {medicion.estatura}m")
            print(f"  IMC: {medicion.imc:.2f} - {medicion.clasificacion_imc}")
            print(f"  Grasa: {medicion.porcentaje_grasa}% | Músculo: {medicion.porcentaje_musculo}%")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

# ==================== OPCIÓN 5: GESTIÓN DE CLASES GRUPALES ====================
def gestionar_clases_grupales():
    while True:
        print("\n--- Gestión de Clases Grupales ---")
        print("1. Crear Clase Grupal")
        print("2. Listar Clases Grupales")
        print("3. Matricular Cliente en Clase")
        print("4. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            crear_clase_grupal()
        elif opcion == "2":
            listar_clases_grupales()
        elif opcion == "3":
            matricular_cliente_clase()
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")

def crear_clase_grupal():
    if not sucursales:
        print("❌ Primero debe crear una sucursal")
        return
    
    print("\n--- Crear Nueva Clase Grupal ---")
    print("Seleccione la sucursal:")
    listar_sucursales()
    
    try:
        sucursal_idx = int(input("Número de sucursal: ")) - 1
        sucursal_seleccionada = sucursales[sucursal_idx]
        
        if not sucursal_seleccionada.instructores:
            print("❌ No hay instructores en esta sucursal")
            return
        
        codigo = input("Código de la clase: ")
        # Verificar si el código ya existe
        for clase in clases_grupales:
            if clase.codigo == codigo:
                print("❌ Ya existe una clase con ese código")
                return
        
        capacidad = int(input("Capacidad máxima: "))
        salon = input("Salón: ")
        horario = input("Horario: ")
        
        print("\nTipos de clase disponibles:")
        for i, tipo in enumerate(ESPECIALIDADES, 1):
            print(f"{i}. {tipo}")
        
        tipo_idx = int(input("Seleccione el tipo de clase: ")) - 1
        tipo_clase = ESPECIALIDADES[tipo_idx]
        
        # Mostrar instructores con esa especialidad
        instructores_especialidad = [inst for inst in sucursal_seleccionada.instructores 
                                   if tipo_clase in inst.especialidades]
        
        if not instructores_especialidad:
            print(f"❌ No hay instructores con especialidad en {tipo_clase}")
            return
        
        print(f"\nInstructores de {tipo_clase}:")
        for i, inst in enumerate(instructores_especialidad, 1):
            print(f"{i}. {inst.nombre}")
        
        instructor_idx = int(input("Seleccione instructor: ")) - 1
        instructor_seleccionado = instructores_especialidad[instructor_idx]
        
        nueva_clase = ClaseGrupal(codigo, capacidad, salon, horario, tipo_clase, instructor_seleccionado)
        clases_grupales.append(nueva_clase)
        sucursal_seleccionada.clases_grupales.append(nueva_clase)
        print("✅ Clase grupal creada exitosamente")
        
    except (ValueError, IndexError):
        print("❌ Datos inválidos")

def listar_clases_grupales():
    if not clases_grupales:
        print("No hay clases grupales registradas")
        return
    
    print("\n--- Clases Grupales Registradas ---")
    for i, clase in enumerate(clases_grupales, 1):
        cupos_disponibles = clase.capacidad - len(clase.clientes_inscritos)
        print(f"{i}. {clase.tipo} - Código: {clase.codigo}")
        print(f"   Instructor: {clase.instructor.nombre} | Horario: {clase.horario}")
        print(f"   Cupos: {cupos_disponibles}/{clase.capacidad} | Salón: {clase.salon}")
        print()

def matricular_cliente_clase():
    if not clientes or not clases_grupales:
        print("❌ No hay clientes o clases grupales registradas")
        return
    
    print("Seleccione el cliente:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        # Verificar máximo de clases
        if len(cliente_seleccionado.clases_inscritas) >= 3:
            print("❌ El cliente ya tiene el máximo de 3 clases")
            return
        
        print("\nClases disponibles:")
        clases_disponibles = [clase for clase in clases_grupales 
                            if len(clase.clientes_inscritos) < clase.capacidad]
        
        if not clases_disponibles:
            print("❌ No hay clases con cupos disponibles")
            return
        
        for i, clase in enumerate(clases_disponibles, 1):
            cupos = clase.capacidad - len(clase.clientes_inscritos)
            print(f"{i}. {clase.tipo} - Cupos: {cupos} - Horario: {clase.horario}")
        
        clase_idx = int(input("Seleccione clase: ")) - 1
        clase_seleccionada = clases_disponibles[clase_idx]
        
        # Verificar que no esté ya matriculado
        if clase_seleccionada in cliente_seleccionado.clases_inscritas:
            print("❌ El cliente ya está matriculado en esta clase")
            return
        
        # Matricular
        cliente_seleccionado.clases_inscritas.append(clase_seleccionada)
        clase_seleccionada.clientes_inscritos.append(cliente_seleccionado)
        print(f"✅ Cliente matriculado en {clase_seleccionada.tipo} exitosamente")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

# ==================== OPCIÓN 6: GENERAR RUTINAS ====================
def gestionar_rutinas():
    while True:
        print("\n--- Generar Rutinas ---")
        print("1. Crear/Modificar Rutina")
        print("2. Ver Rutina de Cliente")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")
        
        if opcion == "1":
            crear_modificar_rutina()
        elif opcion == "2":
            ver_rutina_cliente()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")

def crear_modificar_rutina():
    if not clientes:
        print("❌ No hay clientes registrados")
        return
    
    print("Seleccione el cliente:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        print(f"\n--- Crear Rutina para {cliente_seleccionado.nombre} ---")
        print("Ingrese los ejercicios para cada área:")
        
        ejercicios_por_area = {}
        for area in AREAS_CUERPO:
            ejercicios = input(f"{area}: ").split(',')
            ejercicios_por_area[area] = [ej.strip() for ej in ejercicios if ej.strip()]
        
        # Crear o sobrescribir rutina
        nueva_rutina = Rutina(ejercicios_por_area)
        cliente_seleccionado.rutina_actual = nueva_rutina
        print("✅ Rutina creada/actualizada exitosamente")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

def ver_rutina_cliente():
    if not clientes:
        print("❌ No hay clientes registrados")
        return
    
    print("Seleccione el cliente:")
    listar_clientes()
    
    try:
        cliente_idx = int(input("Número de cliente: ")) - 1
        cliente_seleccionado = clientes[cliente_idx]
        
        if not cliente_seleccionado.rutina_actual:
            print("❌ El cliente no tiene rutina asignada")
            return
        
        print(f"\n--- Rutina Actual de {cliente_seleccionado.nombre} ---")
        rutina = cliente_seleccionado.rutina_actual
        for area, ejercicios in rutina.ejercicios_por_area.items():
            print(f"\n{area}:")
            for i, ejercicio in enumerate(ejercicios, 1):
                print(f"  {i}. {ejercicio}")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida")

# ==================== FUNCIÓN PRINCIPAL ====================
def main():
    print("¡Bienvenido al Sistema PowerLab!")
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            gestionar_sucursales()
        elif opcion == "2":
            gestionar_instructores()
        elif opcion == "3":
            gestionar_clientes()
        elif opcion == "4":
            gestionar_mediciones()
        elif opcion == "5":
            gestionar_clases_grupales()
        elif opcion == "6":
            gestionar_rutinas()
        elif opcion == "7":
            print("¡Gracias por usar PowerLab System!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()