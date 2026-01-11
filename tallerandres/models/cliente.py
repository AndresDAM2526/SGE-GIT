
from odoo import models,fields,api

class cliente(models.Model):
    __name__='res.partner'
    _description = 'Modelo donde se guardan los datos de los clientes'
    _inherit='res.partner'

    id_vehiculo=fields.One2many(string="Vehiculo",comodel_name="tallerandres.vehiculo",inverse_name="id_cliente")