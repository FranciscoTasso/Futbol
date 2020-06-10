from odoo import models, fields, api

class Posiciones_Wirard(models.TransientModel):
    _name = 'posiciones.wizard'

    temporada=fields.Integer(string="Temporada",required=True)

    
    def confirm(self):
        self.env['futbol.posiciones'].with_context(temporada = self.temporada).cargar_posiciones()
