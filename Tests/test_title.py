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

def test_title(driver):

    expected_title = "Eddy's Living"  
    report_status = "Fallo"
    report_description = ""

    try:
     
        driver.get("file:///C:/Users/edisl/OneDrive/Desktop/Creación de Prueba Automatizada/Eddy's Living/index.html") 
        driver.maximize_window()

     
        actual_title = driver.title
        if actual_title == expected_title:
            report_status = "Éxito"
            report_description = f"El título de la página coincide: '{actual_title}'."
        else:
            report_status = "Fallo"
            report_description = f"El título esperado era '{expected_title}', pero se obtuvo '{actual_title}'."


        timestamp = time.strftime("%Y%m%d-%H%M%S")
        formatted_timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        reports_folder = os.path.join(os.getcwd(), "Reports")  
        screenshots_folder = os.path.join(os.getcwd(), "Screenshots")  

        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)

        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)


        screenshot_filename = f"Test_title_{formatted_timestamp}.png"
        report_filename = f"Test_title_{formatted_timestamp}.html"

        screenshot_path = os.path.join(screenshots_folder, screenshot_filename)
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")

    
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

    except Exception as e:
        print(f"Error durante la prueba: {e}")
