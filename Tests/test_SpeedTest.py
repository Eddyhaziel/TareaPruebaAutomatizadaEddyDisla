import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pytest


@pytest.fixture(scope="module")
def driver():
    service = Service('../EdgeWebDriver/msedgedriver.exe')  
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_page_load_speed(driver):
   
    max_load_time = 3  
    url = "file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html"  

 
    screenshots_folder = os.path.join(os.getcwd(), "Screenshots")
    reports_folder = os.path.join(os.getcwd(), "Reports")

    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

   
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"speedtest_{timestamp}.png"
    report_filename = f"speedtest_{timestamp}.html"

   
    screenshot_path = os.path.join(screenshots_folder, screenshot_filename)
    report_path = os.path.join(reports_folder, report_filename)

   
    start_time = time.time()
    driver.get(url)
    driver.maximize_window()
    end_time = time.time()
    load_time = end_time - start_time

   
    if load_time <= max_load_time:
        status = "Éxito"
        description = f"La página cargó en {load_time:.2f} segundos, cumpliendo el umbral de {max_load_time} segundos."
    else:
        status = "Fallo"
        description = f"La página tardó {load_time:.2f} segundos en cargar, superando el umbral de {max_load_time} segundos."


    driver.save_screenshot(screenshot_path)

    
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reporte de Prueba de Velocidad</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center">Reporte de Prueba de Velocidad</h1>
                <table class="table table-bordered table-striped mt-4">
                    <thead class="table-dark">
                        <tr>
                            <th>Estado</th>
                            <th>Descripción</th>
                            <th>Captura</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{status}</td>
                            <td>{description}</td>
                            <td><img src="../Screenshots/{screenshot_filename}" alt="Captura de Pantalla" width="300"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """)

    print(f"Reporte generado: {report_path}")
    print(f"Captura de pantalla guardada: {screenshot_path}")
