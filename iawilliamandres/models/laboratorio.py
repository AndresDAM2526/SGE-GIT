from odoo import models, fields, api

class laboratorio(models.Model):
    _name='iawilliamandres.laboratorio'
    _description="iawilliamandres.laboratorio"

    nombre=fields.Char(string="Nombre",required=True)
    pais=fields.Selection([("ES","España"),("AL","Alemania"),("EE.UU","Estados Unidos"),("JP","Japón")],string="País")
    tipo=fields.Selection([("INV","Investigación"),("PROD","Producción"),("CL","Cloud")],string="Tipo")

    proyectos_id=fields.One2many(string="Proyectos",comodel_name="iawilliamandres.proyecto",inverse_name="laboratorios_id")