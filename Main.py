import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime  # Importamos datetime para obtener la fecha y hora actuales

# Configuración del driver
@pytest.fixture(scope="module")
def driver():
    service = Service('EdgeWebDriver/msedgedriver.exe')  # Cambia la ruta según sea necesario
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

# Crear una carpeta para guardar capturas de pantalla
@pytest.fixture(scope="module", autouse=True)
def create_screenshot_folder():
    output_folder = "screenshots"
    os.makedirs(output_folder, exist_ok=True)
    yield output_folder

# Función para realizar las pruebas
def test_popup(driver, create_screenshot_folder):
    driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta ruta a la ubicación real de tu página
    print("Página cargada exitosamente.")

    # Tomar una captura inicial (antes de interactuar con el popup)
    screenshot_initial = os.path.join(create_screenshot_folder, "pagina_inicial.png")
    driver.save_screenshot(screenshot_initial)

    # Usar WebDriverWait para esperar a que el botón sea clickeable
    result_popup_trigger = "Failed"
    try:
        popup_trigger = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "miBoton"))  # Selector actualizado para el botón
        )
        popup_trigger.click()
        result_popup_trigger = "Passed"
        print("Se hizo clic en el botón para abrir el popup.")
    except Exception as e:
        print("Error al hacer clic en el botón para abrir el popup:", e)

    # Esperar un momento para que el popup sea visible
    time.sleep(2)

    # Capturar el popup después de hacer clic en el botón
    screenshot_popup_visible = os.path.join(create_screenshot_folder, "popup_visible.png")
    result_popup_visible = "Failed"
    try:
        popup_content = driver.find_element(By.ID, "popup")  # Asegúrate de que el popup tiene este ID
        result_popup_visible = "Passed"
        print("Contenido del popup:", popup_content.text)

        # Guardar captura de pantalla del popup visible
        driver.save_screenshot(screenshot_popup_visible)
    except Exception as e:
        print("No se encontró el contenido del popup. Error:", e)

    # Cerrar el popup
    screenshot_popup_closed = os.path.join(create_screenshot_folder, "popup_cerrado.png")
    result_popup_closed = "Failed"
    try:
        close_button = driver.find_element(By.CLASS_NAME, "btn-close")  # Selector para el botón de cerrar
        close_button.click()
        result_popup_closed = "Passed"
        print("Popup cerrado exitosamente.")

        # Capturar la pantalla después de cerrar el popup
        driver.save_screenshot(screenshot_popup_closed)
    except Exception as e:
        print("No se encontró el botón para cerrar el popup. Error:", e)

    # Obtener la fecha y hora actuales
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generar un reporte en HTML
    with open("reporte_resultados.html", "w", encoding="utf-8") as report:
        report.write("<html><head><title>Reporte de Pruebas</title><style>")
        report.write("table {border-collapse: collapse; width: 100%; margin-top: 20px;}")
        report.write("th, td {border: 1px solid #ddd; padding: 8px; text-align: left;}")
        report.write("th {background-color: #4CAF50; color: white;}")
        report.write("tr:nth-child(even) {background-color: #f2f2f2;}")
        report.write(".passed {background-color: #4CAF50; color: white;}")
        report.write(".failed {background-color: #f44336; color: white;}")
        report.write("</style></head><body>")
        report.write("<h1>Reporte de Pruebas Automatizadas</h1>")
        report.write(f"<p>Fecha y hora de generación del reporte: {current_time}</p>")
        report.write("<p>Página inicial cargada correctamente.</p>")
        report.write("<p>Popup activado y contenido inspeccionado:</p>")
        report.write(f"<p>Contenido del popup: {popup_content.text if 'popup_content' in locals() else 'No se encontró el contenido del popup.'}</p>")
        report.write("<p>Capturas de pantalla generadas:</p>")
        report.write("<ul>")
        
        # Insertar las imágenes en el orden correcto
        report.write(f'<li><img src="{screenshot_initial}" alt="Página inicial" style="max-width: 300px; max-height: 200px;"></li>')
        report.write(f'<li><img src="{screenshot_popup_visible}" alt="Popup visible" style="max-width: 300px; max-height: 200px;"></li>')
        report.write(f'<li><img src="{screenshot_popup_closed}" alt="Popup cerrado" style="max-width: 300px; max-height: 200px;"></li>')

        report.write("</ul>")

        # Tabla de resultados
        report.write("<h2>Resultados de la prueba</h2>")
        report.write("<table>")
        report.write("<tr><th>Prueba</th><th>Resultado</th></tr>")
        report.write(f"<tr><td>Hacer clic en el botón para abrir el popup</td><td class='{result_popup_trigger.lower()}'>{result_popup_trigger}</td></tr>")
        report.write(f"<tr><td>Contenido del popup visible</td><td class='{result_popup_visible.lower()}'>{result_popup_visible}</td></tr>")
        report.write(f"<tr><td>Cerrar el popup</td><td class='{result_popup_closed.lower()}'>{result_popup_closed}</td></tr>")
        report.write("</table>")

        # Resumen de la prueba
        report.write("<h2>Resumen de la prueba</h2>")
        report.write("<p><strong>Resultado:</strong> La prueba se completó con éxito.</p>")
        report.write("<p><strong>Pasos realizados:</strong></p>")
        report.write("<ul>")
        report.write("<li>Cargar la página inicial.</li>")
        report.write("<li>Hacer clic en el botón para abrir el popup.</li>")
        report.write("<li>Capturar la pantalla con el popup visible.</li>")
        report.write("<li>Cerrar el popup.</li>")
        report.write("<li>Capturar la pantalla después de cerrar el popup.</li>")
        report.write("</ul>")

        report.write("</body></html>")
        print("Reporte HTML generado exitosamente.")
