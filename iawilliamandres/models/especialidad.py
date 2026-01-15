from odoo import models, fields, api

class especialidad(models.Model):
    _name='iawilliamandres.especialidad'
    _description='iawilliamandres.especialidad'

    nombre=fields.Char(string="Nombre",required=True)
    proyectos_id=fields.One2many(string="Proyectos",comodel_name="iawilliamandres.proyecto",inverse_name="especialidades_id")
    cientificos_id=fields.One2many(string="Científicos",comodel_name="iawilliamandres.cientifico",inverse_name="especialidades_id")