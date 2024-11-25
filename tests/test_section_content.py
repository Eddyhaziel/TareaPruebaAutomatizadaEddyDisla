import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time

# Configuración del driver
@pytest.fixture(scope="module")
def driver():
    service = Service('../EdgeWebDriver/msedgedriver.exe')  # Cambia la ruta según sea necesario
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

# Crear una carpeta para guardar capturas de pantalla
@pytest.fixture(scope="module", autouse=True)
def create_screenshot_folder():
    output_folder = "screenshots"
    os.makedirs(output_folder, exist_ok=True)
    yield output_folder

# Función para verificar el contenido de una sección
def test_section_content(driver, create_screenshot_folder):
    # Cargar la página
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")
    print("Página cargada exitosamente.")

    # Tomar captura de la sección de contenido
    try:
        section_content = driver.find_element(By.ID, "seccion-contenido")  # Asegúrate de que la sección tiene este ID
        screenshot_section = os.path.join(create_screenshot_folder, "section_content_visible.png")
        driver.save_screenshot(screenshot_section)
        result = "PASÓ" if section_content.is_displayed() else "FALLÓ"
        print("Sección de contenido verificada.")
    except Exception as e:
        result = "FALLÓ"
        screenshot_section = ""
        print("Error al verificar la sección de contenido:", e)

    # Obtener la fecha y hora
    test_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Llamar a la función para generar y actualizar el reporte HTML
    generate_html_report("Verificar Contenido de la Sección", result, "Contenido visible de la sección", test_datetime, screenshot_section)

    # Esperar 2 segundos antes de finalizar
    time.sleep(2)

# Función para generar el reporte HTML con los resultados acumulados
def generate_html_report(test_name, result, description, test_datetime, screenshot):
    # Verificar si el archivo HTML existe; si no, crearlo con la estructura base
    if not os.path.exists("resultados_pruebas.html"):
        with open("resultados_pruebas.html", "w", encoding="utf-8") as report:
            report.write("<html><head><title>Reporte de Pruebas</title>")
            report.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">')
            report.write("</head><body>")
            report.write("<div class='container mt-5'>")
            report.write("<h1>Reporte de Pruebas Automatizadas</h1>")
            report.write(f"<p><strong>Fecha y hora de generación del reporte: {test_datetime}</strong></p>")
            report.write("<table class='table table-striped table-bordered'>")
            report.write("<thead><tr><th>Prueba</th><th>Resultado</th><th>Descripción</th><th>Fecha y Hora</th></tr></thead><tbody>")
            report.write("</tbody></table>")
            report.write("</div>")
            report.write("</body></html>")

    # Agregar el resultado de la prueba al archivo HTML
    with open("resultados_pruebas.html", "r+", encoding="utf-8") as report:
        report.seek(0, os.SEEK_END)
        report.write("<tr>")
        report.write(f"<td>{test_name}</td>")
        report.write(f"<td>{result}</td>")
        report.write(f"<td>{description}</td>")
        report.write(f"<td>{test_datetime}</td>")
        report.write("</tr>")
    print("Reporte HTML actualizado exitosamente.")
