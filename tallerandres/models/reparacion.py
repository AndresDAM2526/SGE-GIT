
from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError

class reparacion(models.Model):
    _name='tallerandres.reparacion'
    _description='Modelo donde se guardan las reparaciones'

    fecha_inicio=fields.Date(string="Fecha inicio",help="Fecha inicio",default=lambda fecha: date.today())
    fecha_fin=fields.Date(string="Fecha fin",required=True,help="Fecha fin")
    descripcion=fields.Text(string="Descripcion",help="Descripcion")
    total=fields.Float(string="Total",compute="_get_total",help="Total")
    id_vehiculo=fields.Many2one("tallerandres.vehiculo",string="Vehículo",required=True,ondelete="cascade")
    id_tarea=fields.One2many(string="Tareas",comodel_name="tallerandres.tarea",inverse_name="id_reparacion")

    @api.depends('id_tarea')
    def _get_total(self):
        for reparacion in self:
            tareas=self.env['tallerandres.tarea'].search([('id_reparacion','=',reparacion.id)])
            suma=0
            for tarea in tareas:
                suma+=tarea.total
            reparacion.total=suma

    @api.constrains('fecha_inicio','fecha_fin')
    def _check_fechas(self):
        for reparacion in self:
            if reparacion.fecha_inicio < date.today() or reparacion.fecha_fin < date.today():
                raise ValidationError("Las fechas no pueden ser anteriores al dia actual")