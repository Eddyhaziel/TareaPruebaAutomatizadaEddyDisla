import os
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    service = Service('../EdgeWebDriver/msedgedriver.exe') 
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_access_sales_section(driver):
 
    expected_title = "Eddy's Living"  
    report_status = "Fallo"
    report_description = "No se pudo cargar correctamente la sección de ventas o no cumple con los criterios."

    try:
       
        driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html")
        driver.maximize_window() 
        time.sleep(2)  

  
        actual_title = driver.title
        if actual_title == expected_title:
           
            mesas_header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h5[@class='pb-3' and text()='Mesas']"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", mesas_header)
            time.sleep(2) 

           
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            formatted_timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            screenshots_folder = os.path.join(os.getcwd(), "Screenshots")
            reports_folder = os.path.join(os.getcwd(), "Reports")

            if not os.path.exists(screenshots_folder):
                os.makedirs(screenshots_folder)

            if not os.path.exists(reports_folder):
                os.makedirs(reports_folder)

            screenshot_filename = f"SecVentas_{formatted_timestamp}.png"
            screenshot_path = os.path.join(screenshots_folder, screenshot_filename)
            driver.save_screenshot(screenshot_path)
            print(f"Captura de pantalla guardada en: {screenshot_path}")

          
            report_status = "Éxito"
            report_description = "La sección de ventas carga correctamente."

         
            report_title = "Reporte de Prueba Automatizada - Sección de Ventas"
            report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report_filename = f"SecVentas_{formatted_timestamp}.html"
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
                                    <th>Captura</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>{report_time}</td>
                                    <td>{report_status}</td>
                                    <td>{report_description}</td>
                                    <td><img src="../Screenshots/{screenshot_filename}" alt="Captura de Pantalla" width="300"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </body>
                </html>
                """)
            print(f"Reporte generado en: {report_html_path}")

        else:
            print("El título de la página no coincide con el esperado.")

    except Exception as e:
        print(f"Error durante la prueba: {e}")
