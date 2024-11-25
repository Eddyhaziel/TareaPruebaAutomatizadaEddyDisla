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

# Lista para almacenar los resultados de las pruebas
results = []

# Función para verificar el footer
def test_footer(driver, create_screenshot_folder):
    # Cargar la página
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta ruta
    print("Página cargada exitosamente.")

    # Desplazarse hasta el footer
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Desplazamiento hasta el footer realizado.")

    # Tomar captura del footer
    screenshot_footer = os.path.join(create_screenshot_folder, "footer_visible.png")
    driver.save_screenshot(screenshot_footer)
    print("Captura del footer tomada.")

    # Verificar si el footer es visible (comprobamos si el elemento está en la parte inferior)
    try:
        footer = driver.find_element(By.TAG_NAME, "footer")
        footer_visible = "PASÓ" if footer.is_displayed() else "FALLÓ"
    except Exception as e:
        footer_visible = "FALLÓ"
        print("Error al verificar el footer:", e)

    # Guardar el resultado en la lista con la fecha y hora
    test_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append({
        "Prueba": "Verificar Footer",
        "Resultado": footer_visible,
        "Descripción": "Footer visible en la página",
        "Fecha y Hora": test_datetime,
        "Captura": screenshot_footer  # La captura sigue siendo guardada pero no mostrada en el reporte
    })
    
    # Esperar 2 segundos antes de finalizar
    time.sleep(2)

    # Llamar a la función para generar el reporte HTML acumulativo
    generate_html_report()

# Función para generar el reporte HTML con los resultados acumulados
def generate_html_report():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear el archivo HTML si no existe
    if not os.path.exists("resultados_pruebas.html"):
        with open("resultados_pruebas.html", "w", encoding="utf-8") as report:
            report.write("<html><head><title>Reporte de Pruebas</title>")
            report.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">')  # Bootstrap
            report.write("</head><body>")
            report.write("<div class='container mt-5'>")
            report.write("<h1>Reporte de Pruebas Automatizadas</h1>")
            report.write(f"<p><strong>Fecha y hora de generación del reporte: {current_time}</strong></p>")
            report.write("<table class='table table-striped table-bordered'>")
            report.write("<thead><tr><th>Prueba</th><th>Resultado</th><th>Descripción</th><th>Fecha y Hora</th></tr></thead><tbody>")
            report.write("</tbody></table>")
            report.write("</div>")
            report.write("</body></html>")
    
    # Actualizar el archivo HTML con los resultados acumulados
    with open("resultados_pruebas.html", "r+", encoding="utf-8") as report:
        # Mover el cursor al final para agregar los resultados
        report.seek(0, os.SEEK_END)
        
        # Agregar los resultados de las pruebas
        for result in results:
            report.write("<tr>")
            report.write(f"<td>{result['Prueba']}</td>")
            report.write(f"<td>{result['Resultado']}</td>")
            report.write(f"<td>{result['Descripción']}</td>")
            report.write(f"<td>{result['Fecha y Hora']}</td>")
            report.write("</tr>")

    print("Reporte HTML actualizado exitosamente.")
