from odoo import models,fields,api

class marca(models.Model):
    _name='tallerandres.marca'
    _description='Modelo donde se guardan las marcas'

    name=fields.Char(string='Marca',required=True,help="Marca")