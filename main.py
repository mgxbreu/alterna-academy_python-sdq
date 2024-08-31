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
        # Added field name ("No encontrado") for the times in which the company is not found
        fieldnames = ["rnc", "nombre_comercial", "regimen_pago", "estado", "actividad_economica", "no_encontrado"]

        csv_writer = csv.DictWriter(institution_csv, fieldnames=fieldnames)
        csv_writer.writeheader()

        for rnc in rnc_list:
            await browser_navigation.look_up_rnc(rnc)
            # Added if-else statement to handle different element when company does not show up, also created different function
            try:
                if await browser_navigation.first_page.querySelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)"):
                    extracted_data = await browser_navigation.extract_data(rnc)
                    csv_writer.writerow(extracted_data)
                else:
                    await browser_navigation.first_page.querySelector("#ctl00_cphMain_lblInformacion")
                    extracted_data2 = await browser_navigation.extract_data2(rnc)
                    csv_writer.writerow(extracted_data2)
            except errors.TimeoutError as error:
                continue

asyncio.get_event_loop().run_until_complete(main())

# if __name__ == "__main__":
#     asyncio.run(main())
