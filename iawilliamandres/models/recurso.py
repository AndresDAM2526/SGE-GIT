from odoo import models, fields, api

class recurso(models.Model):
    _name='iawilliamandres.recurso'
    _description='iawilliamandres.recurso'

    nombre=fields.Char(string="Nombre",required=True)
    cantidad_disponible=fields.Integer(string="Cantidad disponible",default=0)

    proyectos_id=fields.Many2many(comodel_name="iawilliamandres.proyecto",relation="proyectos_recursos",column1="recurso_id",column2="proyecto_id",string="Proyectos")