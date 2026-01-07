
from odoo import models,fields,api

class reparacion(models.Model):
    _name='tallerandres.reparacion'
    _description='Modelo donde se guardan las reparaciones'

    fecha_inicio=fields.Date(string="Fecha inicio",required=True,help="Fecha inicio")
    fecha_fin=fields.Date(string="Fecha fin",required=True,help="Fecha fin")
    descripcion=fields.Text(string="Descripcion",help="Descripcion")
    total=fields.Float(string="Total",compute="_get_total",help="Total")
    id_vehiculo=fields.Many2one("tallerandres.vehiculo",string="Vehículo",required=True,ondelete="cascade")
    id_tarea=fields.One2many(string="Tareas",comodel_name="tallerandres.tarea",inverse_name="id_reparacion")

