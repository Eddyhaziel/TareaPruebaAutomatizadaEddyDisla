import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture(scope="module")
def driver():
    service = Service('../EdgeWebDriver/msedgedriver.exe') 
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_access_home_page(driver):
    
    expected_title = "Eddy's Living" 
    report_status = "Fallo"
    report_description = "La página no carga correctamente o no contiene todos sus elementos."

    try:
       
        driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")  # Cambia esta URL según tu página local
        driver.maximize_window()  

       
        actual_title = driver.title
        if actual_title == expected_title:
            report_status = "Éxito"
            report_description = "La página carga correctamente y tiene todos sus elementos."

        
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        formatted_timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        reports_folder = os.path.join(os.getcwd(), "Reports") 
        screenshots_folder = os.path.join(os.getcwd(), "Screenshots") 

        
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)

        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)

       
        screenshot_filename_1 = f"AccesoWebInicio_{formatted_timestamp}.png"
        screenshot_filename_2 = f"AccesoWebFinal_{formatted_timestamp}.png"
        report_filename = f"AccesoWeb_{formatted_timestamp}.html"

        screenshot_path_1 = os.path.join(screenshots_folder, screenshot_filename_1)
        screenshot_path_2 = os.path.join(screenshots_folder, screenshot_filename_2)

        driver.save_screenshot(screenshot_path_1)
        print(f"Captura de pantalla 1 guardada en: {screenshot_path_1}")

       
        footer = driver.find_element(By.TAG_NAME, "footer")
        actions = ActionChains(driver)
        actions.move_to_element(footer).perform()

      
        time.sleep(5)

        
        driver.save_screenshot(screenshot_path_2)
        print(f"Captura de pantalla 2 guardada en: {screenshot_path_2}")

       
        report_title = "Reporte de Prueba Automatizada"
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        report_html_path = os.path.join(reports_folder, report_filename)

        
        with open(report_html_path, "w", encoding="utf-8") as report_file:
            report_file.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{report_title}</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container mt-5">
                    <h1 class="text-center">{report_title}</h1>
                    <table class="table table-bordered table-striped mt-4">
                        <thead class="table-dark">
                            <tr>
                                <th>Hora</th>
                                <th>Estado</th>
                                <th>Descripción</th>
                                <th>Captura 1</th>
                                <th>Captura 2</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{report_time}</td>
                                <td>{report_status}</td>
                                <td>{report_description}</td>
                                <td><img src="../Screenshots/{screenshot_filename_1}" alt="Captura de Pantalla 1" width="300"></td>
                                <td><img src="../Screenshots/{screenshot_filename_2}" alt="Captura de Pantalla 2" width="300"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
            """)

        print(f"Reporte generado en: {report_html_path}")

    except Exception as e:
        print(f"Error durante la prueba: {e}")
