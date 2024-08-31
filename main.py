from utils.csv import extract_rnc_data
from pyppeteer import launch, errors
import asyncio
from classes.browser_navigation import BrowserNavigation
import csv

async def main():
    rnc_list = extract_rnc_data()
    browser_navigation = BrowserNavigation()
    await browser_navigation.navigate()

    # rnc = "132663292"
   

    with open("institution_data.csv", mode="w", newline="") as institution_csv:
        fieldnames = ["rnc", "nombre_comercial", "regimen_pago", "estado", "actividad_economica"]

        csv_writer = csv.DictWriter(institution_csv, fieldnames=fieldnames)
        csv_writer.writeheader()

        for rnc in rnc_list:
            await browser_navigation.look_up_rnc(rnc)
            try:
                await browser_navigation.first_page.waitForSelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)")
                extracted_data = await browser_navigation.extract_data(rnc)
                csv_writer.writerow(extracted_data)
            except errors.TimeoutError as error:
                continue

asyncio.get_event_loop().run_until_complete(main())

# if __name__ = 