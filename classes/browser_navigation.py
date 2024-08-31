from pyppeteer import launch
import asyncio
import unidecode

# Included no_encontrado in import variables
from utils.consts import nombre_comercial, regimen_pago, estado, actividad_economica, dgii_url, rnc_input_selector, search_button_selector, no_encontrado

class BrowserNavigation():
    def __init__(self):
        self.browser = None
        self.first_page = None

    async def set_up_browser(self):
        #Add chromium path and set headless to false since browser was not opening
        self.browser = await launch(headless=False, executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        #added this to avoid two tabs being opened
        self.first_page = (await self.browser.pages())[0]


    async def get_first_page(self):
        pages = await self.browser.pages()
        self.first_page = pages[0]

    async def navigate(self):
        await self.set_up_browser()
        await self.get_first_page()
        await self.first_page.goto(dgii_url)

    async def look_up_rnc(self, rnc):
        rnc_input = await self.first_page.querySelector(rnc_input_selector)
        # Added instruction for input field to be double-clicked. That way, previous text can be replaced
        await rnc_input.click(clickCount=2)
        await rnc_input.type(rnc)
        search_button = await self.first_page.querySelector(search_button_selector)
        await search_button.click()
        await asyncio.sleep(3)

    # Added no_encontrado in the return items for it to be filled as N/A, when company is found
    async def extract_data(self, rnc):
        nombre_comercial_value = await self.first_page.evaluate(nombre_comercial)
        regimen_pago_value = await self.first_page.evaluate(regimen_pago)
        estado_value = await self.first_page.evaluate(estado)
        actividad_economica_value = await self.first_page.evaluate(actividad_economica)

        return {
            "rnc": rnc,
            "nombre_comercial": nombre_comercial_value,
            "regimen_pago": regimen_pago_value,
            "estado": estado_value,
            "actividad_economica": unidecode.unidecode(actividad_economica_value),
            "no_encontrado": "N/A"
        }

    async def clear_input(self):
        return ""

    # Created function to handle cases when company is not found
    async def extract_data2(self, rnc):
        no_encontrado_value = await self.first_page.evaluate(no_encontrado)
        return {
            "rnc": rnc,
            "nombre_comercial": "N/A",
            "regimen_pago": "N/A",
            "estado": "N/A",
            "actividad_economica": "N/A",
            "no_encontrado": "No se encontro esta empresa"
        }

