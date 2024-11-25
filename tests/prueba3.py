import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime  # Importamos datetime para obtener la fecha y hora actuales

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

# Función para realizar la prueba de bajar a la mitad de la página y tomar una captura
def test_scroll_and_capture(driver, create_screenshot_folder):
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta ruta a la ubicación real de tu página
    print("Página cargada exitosamente.")
    
    # Tomar una captura inicial (antes de hacer scroll)
    screenshot_initial = os.path.join(create_screenshot_folder, "pagina_inicial.png")
    driver.save_screenshot(screenshot_initial)

    # Realizar scroll a la mitad de la página
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    mid_point = scroll_height / 2
    driver.execute_script(f"window.scrollTo(0, {mid_point});")
    time.sleep(2)  # Esperar a que el scroll se complete
    
    # Tomar una captura después de hacer el scroll
    screenshot_scroll = os.path.join(create_screenshot_folder, "pagina_mitad.png")
    driver.save_screenshot(screenshot_scroll)
    
    # Obtener la fecha y hora actuales
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generar un reporte en HTML
    with open("reporte_resultados.html", "a", encoding="utf-8") as report:
        report.write("<html><head><title>Reporte de Pruebas</title></head><body>")
        report.write("<h1>Reporte de Pruebas Automatizadas</h1>")
        report.write(f"<p>Fecha y hora de generación del reporte: {current_time}</p>")
        report.write("<p>Se ha realizado el scroll hacia la mitad de la página y se han tomado las siguientes capturas:</p>")
        report.write("<ul>")
        report.write(f'<li><img src="{screenshot_initial}" alt="Página inicial" style="max-width: 300px; max-height: 200px;"></li>')
        report.write(f'<li><img src="{screenshot_scroll}" alt="Página a mitad de la página" style="max-width: 300px; max-height: 200px;"></li>')
        report.write("</ul>")
        report.write("</body></html>")
        print("Reporte HTML actualizado exitosamente.")
