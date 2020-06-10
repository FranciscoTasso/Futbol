from odoo import models, fields, api
import http.client
import json


class Posiciones(models.Model):
        _name ='futbol.posiciones'
        _description = ''

        posicion=fields.Integer(string="Posicion")
        equipo=fields.Char(string="Equipo")
        puntos=fields.Integer(string="Puntos")


        @api.model
        def cargar_posiciones(self):
                context = self._context
                temporada = context.get('temporada', False)
                connection = http.client.HTTPConnection('api.football-data.org')
                headers = {'X-Auth-Token': '2112fb197ad2402ebb02466631fe9ab2'}
                connection.request('GET', '/v2/competitions/PL/standings?season=' + str(temporada), None, headers)
                posiciones = json.loads(connection.getresponse().read().decode())
                values = dict()

                for l in posiciones['standings'][0]['table']:
                        values.clear()
                        values['posicion'] = l['position']
                        values['equipo'] = l['team']['name']
                        values['puntos'] = l['points']
                        self.env['futbol.posiciones'].create(values)


