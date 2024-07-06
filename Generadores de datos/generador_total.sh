#!/bin/bash
# ¡Importante! Para poder ejecutar este script exitosamente es necesario tener Python instalado, y la librería Faker.
# No cambiar el orden de los comandos. De otra forma, es muy probable que el script deje de funcionar ya que del orden de ejecución de cada comando depende el funcionamiento del script.

echo "Ejecutando generador_profesores.py..."
python3 generador_profesores.py
echo ""

echo "Ejecutando generador_obra_social.py..."
python3 generador_obra_social.py
echo ""

echo "Ejecutando generador_dependencia.py..."
python3 generador_dependencia.py
echo ""

echo "Ejecutando generador_datos_trabajo.py..."
python3 generador_datos_trabajo.py
echo ""

echo "Ejecutando generador_seguro_de_vida.py..."
python3 generador_seguro_de_vida.py
echo ""

echo "Ejecutando generador_familiar.py..."
python3 generador_familiar.py
echo ""

echo "Ejecutando generador_participaciones_reuniones_cientificas.py..."
python3 generador_participaciones_reuniones_cientificas.py
echo ""

echo "Ejecutando generador_publicaciones.py..."
python3 generador_publicaciones.py
echo ""

echo "Ejecutando generador_antecedentes_profesionales.py..."
python3 generador_antecedentes_profesionales.py
echo ""

echo "Ejecutando generador_titulos.py..."
python3 generador_titulos.py
echo ""

echo "Ejecutando generador_idiomas.py..."
python3 generador_idiomas.py
echo ""

echo "Ejecutando generador_cursos_y_conferencias.py..."
python3 generador_cursos_y_conferencias.py
echo ""

echo "Ejecutando generador_actividades_y_antecedentes.py..."
python3 generador_actividades_y_antecedentes.py
echo ""

echo "Ejecutando generador_antecedentes_extension_universitaria.py..."
python3 generador_antecedentes_extension_universitaria.py
echo ""

echo "Ejecutando generador_actividad_e_investigacion.py..."
python3 generador_actividad_e_investigacion.py
echo ""

echo "Ejecutando generador_antecedentes_docentes.py..."
python3 generador_antecedentes_docentes.py
echo ""

echo "Ejecutando generador_datos_empleador.py..."
python3 generador_datos_empleador.py
echo ""

echo "Ejecutando generador_datos_contacto.py..."
python3 generador_datos_contacto.py
echo ""

echo "Ejecutando generador_declaracion_jurada.py..."
python3 generador_declaracion_jurada.py
echo ""

echo "Ejecutando generador_carga_horaria.py..."
python3 generador_carga_horaria.py
echo ""

echo "Ejecutando generador_datos_cargo.py..."
python3 generador_datos_cargo.py
echo ""

echo "Ejecutando generador_pasividades.py..."
python3 generador_pasividades.py
echo ""

echo "Ejecutando generador_tareas_no_estatales.py..."
python3 generador_tareas_no_estatales.py
echo ""
