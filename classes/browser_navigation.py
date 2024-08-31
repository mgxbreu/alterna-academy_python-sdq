from pyppeteer import launch
import asyncio
import unidecode
from utils.consts import nombre_comercial, regimen_pago, estado, actividad_economica, dgii_url, rnc_input_selector, search_button_selector

class BrowserNavigation():
    def __init__(self):
        self.browser = None
        self.first_page = None

    async def set_up_browser(self):
        self.browser = await launch(headless=True)

    async def get_first_page(self):
        pages = await self.browser.pages()
        self.first_page = pages[0]

    async def navigate(self):
        await self.set_up_browser()
        await self.get_first_page()
        await self.first_page.goto(dgii_url)

    async def look_up_rnc(self, rnc):
        rnc_input = await self.first_page.querySelector(rnc_input_selector)
        await rnc_input.type(rnc)
        search_button = await self.first_page.querySelector(search_button_selector)
        await search_button.click()
        # await asyncio.sleep(3)

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
            "actividad_economica": unidecode.unidecode(actividad_economica_value)
        }
