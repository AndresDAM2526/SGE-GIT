
from odoo import models,fields,api

class tarea(models.Model):
    _name='tallerandres.tarea'
    _description='Modelo donde se guardan las tareas realizadas en cada reparacion'

    name=fields.Char(string="Nombre",required=True,help="Nombre")
    tiempo=fields.Float(string="Tiempo",required=True,help="Tiempo")
    precio_hora=fields.Float(string="Precio por hora",required=True,help="Precio por hora")
    total=fields.Float(string="Total",compute="_get_total",store=True)
    id_reparacion=fields.Many2one("tallerandres.reparacion",string="Reparaciones",required=True,ondelete="cascade")
    id_mecanico=fields.Many2many(comodel_name="tallerandres.mecanico",relation="tarea_mecanico",column1="mecanico_id",column2="tarea_id",string="Mecanicos")

    @api.depends('tiempo','precio_hora')
    def _get_total(self):
        for tarea in self:
            tarea.total=tarea.tiempo*tarea.precio_hora
