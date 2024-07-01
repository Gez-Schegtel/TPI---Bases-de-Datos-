#!/bin/bash

# No cambiar el orden de los comandos. De otra forma, es muy probable que el script deje de funcionar ya que del orden de ejecución de cada comando depende el funcionamiento del script.

echo "Ejecutando generador_profesores.py..."
python3 generador_profesores.py

echo "Ejecutando generador_obrasocial.py..."
python3 generador_obrasocial.py

echo "Ejecutando generador_dependencia.py..."
python3 generador_dependencia.py

echo "Ejecutando generador_datostrabajo.py..."
python3 generador_datostrabajo.py

echo "Ejecutando generador_segurodevida.py..."
python3 generador_segurodevida.py

echo "Ejecutando generador_familiar.py..."
python3 generador_familiar.py

echo "Ejecutando generador_partreucient.py..."
python3 generador_partreucient.py

echo "Ejecutando generador_publicaciones.py..."
python3 generador_publicaciones.py

echo "Ejecutando generador_antecprof.py..."
python3 generador_antecprof.py

echo "Ejecutando generador_titulos.py..."
python3 generador_titulos.py

echo "Ejecutando generador_idiomas.py..."
python3 generador_idiomas.py

echo "Ejecutando generador_cursosyconf.py..."
python3 generador_cursosyconf.py

echo "Ejecutando generador_actyant.py..."
python3 generador_actyant.py

echo "Ejecutando generador_antextuniv.py..."
python3 generador_antextuniv.py

echo "Ejecutando generador_acteinv.py..."
python3 generador_acteinv.py

echo "Ejecutando generador_antdocentes.py..."
python3 generador_antdocentes.py

echo "Ejecutando generador_datosempleador.py..."
python3 generador_datosempleador.py

echo "Ejecutando generador_datoscontacto.py..."
python3 generador_datoscontacto.py

echo "Ejecutando generador_declaracionjurada.py..."
python3 generador_declaracionjurada.py

echo "Ejecutando generador_cargahoraria.py..."
python3 generador_cargahoraria.py

echo "Ejecutando generador_datoscargo.py..."
python3 generador_datoscargo.py

echo "Ejecutando generador_pasividades.py..."
python3 generador_pasividades.py

echo "Ejecutando generador_tareasnoestatales.py..."
python3 generador_tareasnoestatales.py
