nombre_comercial = """
                () => {
                    const data =  document.querySelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)").innerText
                    return data
                }
                """
regimen_pago = """
                () => {
                    const data =  document.querySelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(5) > td:nth-child(2)").innerText
                    return data
                }
                """
estado = """
                () => {
                    const data =  document.querySelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(6) > td:nth-child(2)").innerText
                    return data
                }
                """
actividad_economica = """
                () => {
                    const data =  document.querySelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(7) > td:nth-child(2)").innerText
                    return data
                }
                """

#Added new const for the times in which the data is not found.
no_encontrado = """
                () => { 
                    const data = document.querySelector("#ctl00_cphMain_lblInformacion.innerText")
                    return data
                }
                """

dgii_url = 'https://www.dgii.gov.do/app/WebApps/ConsultasWeb/consultas/rnc.aspx'

rnc_input_selector = "#ctl00_cphMain_txtRNCCedula"

search_button_selector = "#ctl00_cphMain_btnBuscarPorRNC"
