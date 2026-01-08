
from odoo import models,fields,api
from odoo.exceptions import ValidationError

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

    @api.constrains('precio_hora')
    def _check_precio(self):
        for tarea in self:
            if tarea.precio_hora<0:
                raise ValidationError("El precio por hora no puede ser negativo")
            
    @api.constrains('tiempo')
    def _check_tiempo(self):
        for tarea in self:
            if tarea.tiempo>0:
                raise ValidationError("El tiempo no puede ser negativo")