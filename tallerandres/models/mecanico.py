
from odoo import models,fields,api

class mecanico(models.Model):
    _name='tallerandres.mecanico'
    _description='Modelo donde se guardan los mecánicos'

    nombre=fields.Char(string="Nombre",required=True,help="Nombre")
    especialidad=fields.Char(string="Especialidad",help="Especialidad")