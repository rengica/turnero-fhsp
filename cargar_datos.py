from app import app, db, Especialidad, Medico 

with app.app_context():
    # Crear especialidades
    cardiologia = Especialidad(nombre='Cardiología')
    pediatria = Especialidad(nombre='Pediatría')
    medicina_interna = Especialidad(nombre='Medicina interna')
    cirugia_general = Especialidad(nombre='Cirugia general')
    determatologia = Especialidad(nombre='Dermatologia')
    endocrinologia = Especialidad(nombre='Endocrinologia')
    gastroenterologia = Especialidad(nombre='Gastroenterologia')
    ginecoobstetricia = Especialidad(nombre='Ginecoobstetricia')
    cirugia_plastica_y_estetica = Especialidad(nombre='Cirugia plastica y estetica')
    cirugia_vascular = Especialidad(nombre='Cirugia vascular')
    medicina_del_trabajo = Especialidad(nombre='Medicina del trabajo')
    cirugia_de_columna = Especialidad(nombre='Cirugia de columna')
    urologia = Especialidad(nombre='Urologia')
    reumatologia = Especialidad(nombre='Reumatologia')
    otorrinolaringologia = Especialidad(nombre='Otorrinolaringologia')
    ortopedia_yo_traumatologia = Especialidad(nombre='Ortopedia y/o traumatologias')
    oftalmologia = Especialidad(nombre='Oftalmologia')
    neurologia = Especialidad(nombre='Neurologia')
    neumologia = Especialidad(nombre='Neumologia')
    nefralogia = Especialidad(nombre='Nefralogia')
    neurocirugia = Especialidad(nombre='Neurocirugia')
                                    
    

    db.session.add_all([cardiologia, pediatria, medicina_interna, cirugia_general, determatologia, endocrinologia, gastroenterologia, ginecoobstetricia, cirugia_plastica_y_estetica, cirugia_vascular, medicina_del_trabajo, cirugia_de_columna, urologia, reumatologia, otorrinolaringologia, ortopedia_yo_traumatologia, oftalmologia, neurologia, neumologia, nefralogia, neurocirugia])
    db.session.commit()

    # Crear médicos
    med1 = Medico(nombre='Dr. Pedro Pérez', especialidad=cardiologia)
    med2 = Medico(nombre='Dra. Ana Ramírez', especialidad=pediatria)
    med3 = Medico(nombre='Dr. Juan García', especialidad=medicina_interna)
    med4 = Medico(nombre='Dr. x"', especialidad=cirugia_general)
    med5 = Medico(nombre='Dra. e', especialidad=determatologia)
    med6 = Medico(nombre='Dr. r', especialidad=endocrinologia)
    med7 = Medico(nombre='Dr. t', especialidad=gastroenterologia)
    med8 = Medico(nombre='Dr. y', especialidad=ginecoobstetricia)
    med9 = Medico(nombre='Dr. u', especialidad=cirugia_plastica_y_estetica)
    med10 = Medico(nombre='Dr. i', especialidad=cirugia_vascular)
    med11 = Medico(nombre='Dr. o', especialidad=medicina_del_trabajo)
    med12 = Medico(nombre='Dr. p', especialidad=cirugia_de_columna)
    med13 = Medico(nombre='Dr. a', especialidad=urologia)
    med14 = Medico(nombre='Dr. s', especialidad=reumatologia)
    med15 = Medico(nombre='Dr. d', especialidad=otorrinolaringologia)
    med16 = Medico(nombre='Dr. f', especialidad=ortopedia_yo_traumatologia)
    med17 = Medico(nombre='Dr. g', especialidad=oftalmologia)
    med18 = Medico(nombre='Dr. h', especialidad=neurologia)
    med19 = Medico(nombre='Dr. j', especialidad=neumologia)
    med20 = Medico(nombre='Dr. k', especialidad=nefralogia)
    med21 = Medico(nombre='Dr. l', especialidad=neurocirugia)

    db.session.add_all([med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14, med15, med16, med17, med18, med19, med20, med21])
    db.session.commit()



    print("✅ Datos agregados correctamente.")
