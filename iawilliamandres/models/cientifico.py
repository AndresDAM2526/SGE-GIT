from odoo import models, fields, api

class cientifico(models.Model):
    _name='iawilliamandres.cientifico'
    _description='iawilliamandres.cientifico'

    nombre=fields.Char(string="Nombre",required=True)

    proyectos_id=fields.One2many(string="Proyectos",comodel_name="iawilliamandres.proyecto",inverse_name="cientificos_id")
    especialidades_id=fields.Many2one("iawilliamandres.especialidad",string="Especialidades",ondelete="cascade")


    def _get_recursos(self):
        for cientifos in self:
            recursos=self.env['iawilliamandres.recurso'].search([('proyecto_id','=',cientifico.proyectos_id.recursos_id)])




