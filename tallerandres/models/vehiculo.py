
from odoo import models,fields,api

class vehiculo(models.Model):
    _name='tallerandres.vehiculo'
    _description='Modelo donde se guardan los vehículos'

    name=fields.Char(string="Matricula",required=True,help="Matricula")
    id_marca=fields.Many2one("tallerandres.marca",string="Marca",required=True,ondelete="cascade")
    modelo=fields.Char(string="Modelo",help="Modelo")
    id_cliente=fields.Many2one("tallerandres.cliente",string="Cliente",required=True,ondelete="cascade")
    