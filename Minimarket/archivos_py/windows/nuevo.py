fecha_dt = dato[1]
if isinstance(fecha_dt, str):
    fecha_dt = fecha_dt.split('+')[0].strip()
    try:
        fecha_dt = datetime.strptime(fecha_dt, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        try:
            fecha_dt = datetime.strptime(fecha_dt, "%Y-%m-%dT%H:%M:%S")
        except Exception:
            fecha_dt = None
if fecha_dt:
    fecha_separada = fecha_dt.strftime("%d-%m-%Y")
    hora_separada = fecha_dt.strftime("%I:%M %p")
else:
    fecha_separada = ""
    hora_separada = ""