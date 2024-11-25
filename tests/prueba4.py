import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
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

# Función para verificar que la página cargue correctamente
def test_page_load(driver, create_screenshot_folder):
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta ruta a la ubicación real de tu página
    print("Página cargada exitosamente.")
    
    # Verificar que la página cargó correctamente
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        print("La página cargó correctamente.")
        
        # Tomar una captura de pantalla de la página cargada
        screenshot_page_loaded = os.path.join(create_screenshot_folder, "pagina_cargada.png")
        driver.save_screenshot(screenshot_page_loaded)
        
        # Obtener la fecha y hora actuales
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Generar un reporte en HTML
        with open("reporte_resultados.html", "a", encoding="utf-8") as report:
            report.write("<html><head><title>Reporte de Pruebas</title></head><body>")
            report.write("<h1>Reporte de Pruebas Automatizadas</h1>")
            report.write(f"<p>Fecha y hora de generación del reporte: {current_time}</p>")
            report.write("<p>La página cargó correctamente. Se tomó una captura de la página cargada:</p>")
            report.write("<ul>")
            report.write(f'<li><img src="{screenshot_page_loaded}" alt="Página cargada" style="max-width: 300px; max-height: 200px;"></li>')
            report.write("</ul>")
            report.write("</body></html>")
            print("Reporte HTML actualizado exitosamente.")
    except Exception as e:
        print(f"Error al cargar la página: {e}")
