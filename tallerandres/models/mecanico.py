
from odoo import models,fields,api

class mecanico(models.Model):
    _name='tallerandres.mecanico'
    _description='Modelo donde se guardan los mecánicos'

    name=fields.Char(string="Nombre",required=True,help="Nombre")
    especialidad=fields.Char(string="Especialidad",help="Especialidad")
    id_tarea=fields.Many2many(comodel_name="tallerandres.tarea",relation="tarea_mecanico",column1="tarea_id",column2="mecanico_id",string="Tareas")