
from odoo import models,fields,api

class cliente(models.Model):
    _name = 'tallerandres.cliente'
    _description = 'Modelo donde se guardan los datos de los clientes'

    dni=fields.Char(string="DNI",required=True,help="DNI")
    name=fields.Char(string="Nombre completo",required=True,help="Nombre")
    direccion=fields.Char(string="Direccion",help="Dirección")
    id_vehiculo=fields.One2many(string="Vehiculo",comodel_name="tallerandres.vehiculo",inverse_name="id_cliente")