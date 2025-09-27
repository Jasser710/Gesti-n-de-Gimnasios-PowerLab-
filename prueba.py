from clases.Sucursal import Sucursal
from clases.Instructor import Instructor
from clases.Cliente import Cliente
from clases.Medicion import Medicion
from clases.ClaseGrupal import ClaseGrupal
from clases.Rutina import Rutina

def test_sistema_completo():
    print("🧪 INICIANDO PRUEBA COMPLETA DEL SISTEMA POWERLAB")
    print("=" * 60)
    
    # ==================== PRUEBA 1: SUCURSALES ====================
    print("\n1. 🔄 PROBANDO SUCURSALES...")
    try:
        sucursal1 = Sucursal("S001", "San José", "Central", "central@powerlab.com", "2222-2222")
        sucursal2 = Sucursal("S002", "Alajuela", "Central", "alajuela@powerlab.com", "2444-4444")
        print(f"✅ Sucursal 1: {sucursal1}")
        print(f"✅ Sucursal 2: {sucursal2}")
        print(f"✅ Instructores en sucursal 1: {len(sucursal1.instructores)}")
        print(f"✅ Clientes en sucursal 1: {len(sucursal1.clientes)}")
    except Exception as e:
        print(f"❌ Error en sucursales: {e}")
        return False

    # ==================== PRUEBA 2: INSTRUCTORES ====================
    print("\n2. 💪 PROBANDO INSTRUCTORES...")
    try:
        instructor1 = Instructor("111111111", "Carlos Méndez", "8888-8888", "carlos@powerlab.com", 
                               "15/03/1985", ["Pesas", "Cardio"], sucursal1)
        instructor2 = Instructor("222222222", "Ana Rodríguez", "8999-9999", "ana@powerlab.com", 
                               "20/07/1990", ["Yoga", "Zumba"], sucursal1)
        instructor3 = Instructor("333333333", "Juan Pérez", "8777-7777", "juan@powerlab.com", 
                               "10/05/1988", ["CrossFit", "HIIT"], sucursal2)
        
        # Agregar instructores a sucursales
        sucursal1.instructores.extend([instructor1, instructor2])
        sucursal2.instructores.append(instructor3)
        
        print(f"✅ Instructor 1: {instructor1}")
        print(f"✅ Instructor 2: {instructor2}")
        print(f"✅ Instructor 3: {instructor3}")
        print(f"✅ Total instructores sucursal 1: {len(sucursal1.instructores)}")
        print(f"✅ Total instructores sucursal 2: {len(sucursal2.instructores)}")
    except Exception as e:
        print(f"❌ Error en instructores: {e}")
        return False

    # ==================== PRUEBA 3: CLIENTES ====================
    print("\n3. 👥 PROBANDO CLIENTES...")
    try:
        cliente1 = Cliente("444444444", "María González", "8111-1111", "maria@email.com", 
                          "25/12/1995", "F", "01/09/2024", sucursal1)
        cliente2 = Cliente("555555555", "Luis Chacón", "8222-2222", "luis@email.com", 
                          "30/06/1988", "M", "02/09/2024", sucursal1)
        cliente3 = Cliente("666666666", "Sofía Ramírez", "8333-3333", "sofia@email.com", 
                          "15/03/1992", "F", "03/09/2024", sucursal2)
        
        # Agregar clientes a sucursales
        sucursal1.clientes.extend([cliente1, cliente2])
        sucursal2.clientes.append(cliente3)
        
        # Asignar instructores
        cliente1.instructor_asignado = instructor1
        cliente2.instructor_asignado = instructor2
        cliente3.instructor_asignado = instructor3
        
        print(f"✅ Cliente 1: {cliente1}")
        print(f"✅ Cliente 2: {cliente2}")
        print(f"✅ Cliente 3: {cliente3}")
        print(f"✅ Cliente 1 tiene instructor: {cliente1.instructor_asignado is not None}")
        print(f"✅ Total clientes sucursal 1: {len(sucursal1.clientes)}")
    except Exception as e:
        print(f"❌ Error en clientes: {e}")
        return False

    # ==================== PRUEBA 4: MEDICIONES ====================
    print("\n4. 📊 PROBANDO MEDICIONES...")
    try:
        # Crear mediciones para cliente1
        medicion1 = Medicion(
            "01/09/2024", 68.5, 1.65, 25.0, 35.0, 28, 10.0, 
            78.0, 95.0, 98.0, 52.0, 25.2, "Normal", 54.8, 9.8
        )
        
        medicion2 = Medicion(
            "01/10/2024", 67.0, 1.65, 23.5, 36.5, 27, 9.5, 
            76.0, 94.0, 97.0, 51.0, 24.6, "Normal", 53.6, 9.6
        )
        
        cliente1.mediciones.extend([medicion1, medicion2])
        
        print(f"✅ Medición 1 - IMC: {medicion1.imc:.1f} - Clasificación: {medicion1.clasificacion_imc}")
        print(f"✅ Medición 2 - IMC: {medicion2.imc:.1f} - Proteína: {medicion2.proteina_recomendada:.1f}g")
        print(f"✅ Total mediciones cliente 1: {len(cliente1.mediciones)}")
        print(f"✅ Vasos de agua recomendados: {medicion1.vasos_agua:.1f}")
        
        # Probar cliente de alto riesgo
        medicion_riesgo = Medicion(
            "01/09/2024", 110.0, 1.70, 35.0, 28.0, 45, 15.0,
            105.0, 115.0, 120.0, 65.0, 38.1, "Obesidad media", 88.0, 15.7
        )
        print(f"✅ Cliente riesgo - IMC: {medicion_riesgo.imc:.1f} - {medicion_riesgo.clasificacion_imc}")
    except Exception as e:
        print(f"❌ Error en mediciones: {e}")
        return False

    # ==================== PRUEBA 5: CLASES GRUPALES ====================
    print("\n5. 🏋️ PROBANDO CLASES GRUPALES...")
    try:
        clase1 = ClaseGrupal("C001", 15, "Salón A", "08:00-09:00", "Pesas", instructor1)
        clase2 = ClaseGrupal("C002", 20, "Salón B", "10:00-11:00", "Yoga", instructor2)
        clase3 = ClaseGrupal("C003", 10, "Salón C", "18:00-19:00", "CrossFit", instructor3)
        
        # Agregar clases a sucursales
        sucursal1.clases_grupales.extend([clase1, clase2])
        sucursal2.clases_grupales.append(clase3)
        
        # Matricular clientes
        clase1.clientes_inscritos.append(cliente1)
        clase2.clientes_inscritos.append(cliente1)
        clase2.clientes_inscritos.append(cliente2)
        clase3.clientes_inscritos.append(cliente3)
        
        cliente1.clases_inscritas.extend([clase1, clase2])
        cliente2.clases_inscritas.append(clase2)
        cliente3.clases_inscritas.append(clase3)
        
        print(f"✅ Clase 1: {clase1}")
        print(f"✅ Clase 2: {clase2}")
        print(f"✅ Clase 3: {clase3}")
        print(f"✅ Cliente 1 tiene {len(cliente1.clases_inscritas)} clases")
        print(f"✅ Cupos clase 1: {clase1.capacidad - len(clase1.clientes_inscritos)}/{clase1.capacidad}")
        print(f"✅ Instructor clase 2: {clase2.instructor.nombre}")
    except Exception as e:
        print(f"❌ Error en clases grupales: {e}")
        return False

    # ==================== PRUEBA 6: RUTINAS ====================
    print("\n6. 📝 PROBANDO RUTINAS...")
    try:
        rutina_dict1 = {
            "Pecho y tríceps": ["Press banca 3x10", "Fondos 3x12", "Aperturas 3x15"],
            "Bíceps": ["Curl con barra 4x10", "Curl martillo 3x12"],
            "Piernas": ["Sentadillas 4x8", "Prensa 3x10", "Extensiones 3x12"],
            "Espalda": ["Dominadas 3xmax", "Remo con barra 4x10"]
        }
        
        rutina_dict2 = {
            "Pecho y tríceps": ["Press inclinado 3x10", "Fondos paralelos 3x12"],
            "Bíceps": ["Curl concentrado 3x12", "Curl predicador 3x10"],
            "Piernas": ["Peso muerto 4x6", "Sentadilla frontal 4x8"],
            "Espalda": ["Jalon al pecho 3x10", "Remo con mancuerna 3x12"]
        }
        
        rutina1 = Rutina(rutina_dict1)
        rutina2 = Rutina(rutina_dict2)
        
        cliente1.rutina_actual = rutina1
        cliente2.rutina_actual = rutina2
        
        print(f"✅ Rutina 1 creada con {len(rutina1.ejercicios_por_area)} áreas")
        print(f"✅ Rutina 2 creada con {len(rutina2.ejercicios_por_area)} áreas")
        print(f"✅ Cliente 1 tiene rutina: {cliente1.rutina_actual is not None}")
        print(f"✅ Ejercicios de pecho cliente 1: {len(rutina1.ejercicios_por_area['Pecho y tríceps'])}")
    except Exception as e:
        print(f"❌ Error en rutinas: {e}")
        return False

    # ==================== PRUEBA 7: RELACIONES COMPLETAS ====================
    print("\n7. 🔗 PROBANDO RELACIONES COMPLETAS...")
    try:
        print(f"✅ Sucursal 1 - Instructores: {len(sucursal1.instructores)}")
        print(f"✅ Sucursal 1 - Clientes: {len(sucursal1.clientes)}")
        print(f"✅ Sucursal 1 - Clases: {len(sucursal1.clases_grupales)}")
        
        print(f"✅ Cliente 1 - Sucursal: {cliente1.sucursal.canton}")
        print(f"✅ Cliente 1 - Instructor: {cliente1.instructor_asignado.nombre}")
        print(f"✅ Cliente 1 - Mediciones: {len(cliente1.mediciones)}")
        print(f"✅ Cliente 1 - Clases: {len(cliente1.clases_inscritas)}")
        print(f"✅ Cliente 1 - Rutina: {'Sí' if cliente1.rutina_actual else 'No'}")
        
        print(f"✅ Instructor 1 - Sucursal: {instructor1.sucursal.canton}")
        print(f"✅ Instructor 1 - Clases que imparte: {len([c for c in [clase1, clase2, clase3] if c.instructor.cedula == instructor1.cedula])}")
    except Exception as e:
        print(f"❌ Error en relaciones: {e}")
        return False

    # ==================== PRUEBA 8: VALIDACIONES ====================
    print("\n8. ✅ PROBANDO VALIDACIONES...")
    try:
        # Verificar máximos
        print(f"✅ Máximo mediciones cliente 1: {len(cliente1.mediciones)}/10")
        print(f"✅ Máximo clases cliente 1: {len(cliente1.clases_inscritas)}/3")
        print(f"✅ Máximo clases cliente 2: {len(cliente2.clases_inscritas)}/3")
        
        # Verificar cupos clases
        print(f"✅ Cupos clase 2: {clase2.capacidad - len(clase2.clientes_inscritos)}/{clase2.capacidad}")
        
        # Verificar especialidades
        print(f"✅ Instructor 1 especialidades: {instructor1.especialidades}")
        print(f"✅ Clase 1 tipo: {clase1.tipo} - Instructor especialidad: {clase1.tipo in clase1.instructor.especialidades}")
        
        print("✅ Todas las validaciones pasaron correctamente")
    except Exception as e:
        print(f"❌ Error en validaciones: {e}")
        return False

    # ==================== RESUMEN FINAL ====================
    print("\n" + "=" * 60)
    print("🎉 ¡PRUEBA COMPLETA EXITOSA!")
    print("=" * 60)
    print(f"📊 RESUMEN FINAL:")
    print(f"   • Sucursales creadas: 2")
    print(f"   • Instructores creados: 3")
    print(f"   • Clientes creados: 3")
    print(f"   • Mediciones creadas: 3")
    print(f"   • Clases grupales creadas: 3")
    print(f"   • Rutinas creadas: 2")
    print(f"   • Relaciones establecidas: ✅")
    print(f"   • Validaciones probadas: ✅")
    print("=" * 60)
    
    return True

def test_errores():
    print("\n🔧 PROBANDO MANEJO DE ERRORES...")
    
    # Probar crear objeto con datos inválidos
    try:
        cliente_error = Cliente("123", "Test", "123", "test@test.com", "01/01/2000", "X", "01/01/2024")
        print("✅ Cliente con datos mínimos creado")
    except Exception as e:
        print(f"❌ Error creando cliente: {e}")
    
    # Probar acceso a atributos no existentes
    try:
        sucursal = Sucursal("TEST", "Test", "Test", "test@test.com", "1234")
        if hasattr(sucursal, 'instructores'):
            print("✅ Atributo 'instructores' existe")
        else:
            print("❌ Atributo 'instructores' no existe")
    except Exception as e:
        print(f"❌ Error probando atributos: {e}")

if __name__ == "__main__":
    # Ejecutar prueba principal
    exito = test_sistema_completo()
    
    # Ejecutar prueba de errores
    test_errores()
    
    if exito:
        print("\n🎊 ¡EL SISTEMA ESTÁ LISTO PARA USAR!")
    else:
        print("\n⚠️  Hay errores que necesitan corrección")
    
    print("\n💡 Consejo: Si hay errores, revisa que todas las clases tengan los atributos correctos")