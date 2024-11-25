import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Configuración del driver
@pytest.fixture(scope="module")
def driver():
    service = Service('../EdgeWebDriver/msedgedriver.exe')  # Cambia la ruta según sea necesario
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

# Función para actualizar el reporte HTML
def actualizar_reporte_html(prueba, resultado, fecha_hora):
    # Definir la ruta del archivo HTML donde se agregan los resultados
    reporte_html = "reporte_resultados.html"
    
    # Abrir el archivo HTML en modo lectura y luego reescribirlo con los nuevos resultados
    with open(reporte_html, "r", encoding="utf-8") as file:
        contenido_html = file.read()
    
    # Crear la fila de la tabla con los resultados
    fila_html = f"""
    <tr class="{'status-passed' if resultado == 'Pasó' else 'status-failed'}">
        <td>{prueba}</td>
        <td>{resultado}</td>
        <td>{fecha_hora}</td>
    </tr>
    """
    
    # Incluir la fila en la tabla
    contenido_html = contenido_html.replace('</tbody>', fila_html + '</tbody>')
    
    # Guardar el archivo con los cambios
    with open(reporte_html, "w", encoding="utf-8") as file:
        file.write(contenido_html)

# Función de prueba para verificar título
def test_verificar_titulo(driver):
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta ruta a la ubicación real de tu página
    print("Página cargada exitosamente.")
    
    # Verificar si el título de la página es correcto
    expected_title = "Eddy's Living"
    actual_title = driver.title

    # Determinar si pasó o no
    if actual_title == expected_title:
        resultado = "Pasó"
    else:
        resultado = "No pasó"
    
    # Obtener la fecha y hora actuales
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Actualizar el reporte HTML con el resultado
    actualizar_reporte_html("Verificar Título", resultado, current_time)
    
    assert actual_title == expected_title  # Asegúrate de que el título es correcto

