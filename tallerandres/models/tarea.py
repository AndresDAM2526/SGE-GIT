
from odoo import models,fields,api

class tarea(models.Model):
    _name='tallerandres.tarea'
    _description='Modelo donde se guardan las tareas realizadas en cada reparacion'

    nombre=fields.Char(string="Nombre",required=True,help="Nombre")
    tiempo=fields.Float(string="Tiempo",required=True,help="Tiempo")
    precio_hora=fields.Float(string="Precio por hora",required=True,help="Precio por hora")