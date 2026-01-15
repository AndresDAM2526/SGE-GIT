from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError

class proyecto(models.Model):
    _name='iawilliamandres.proyecto'
    _description='iawilliamandres.proyecto'

    titulo=fields.Char(string="titulo",compute="_get_titulo")
    descripcion=fields.Char(string="descripcion",required=True)
    prioridad=fields.Integer(string="prioridad",default=0)
    urgente=fields.Boolean(string="urgente",compute="_get_prioridad")
    en_espera=fields.Boolean(string="en espera",default=True)
    finalizado=fields.Boolean(string="finalizado")
    imagen=fields.Image()
    fecha_creacion=fields.Datetime(default= lambda f: datetime.datetime.now())
    fecha_modificacion=fields.Datetime(default=lambda f:datetime.datetime.now())

    laboratorios_id=fields.Many2one("iawilliamandres.laboratorio",string="Laboratorios",ondelete="cascade")
    cientificos_id=fields.Many2one("iawilliamandres.cientifico",string="Laboratorios",ondelete="cascade")
    especialidades_id=fields.Many2one("iawilliamandres.especialidad",string="Laboratorios",ondelete="cascade")
    recursos_id=fields.Many2many(comodel_name="iawilliamandres.recurso",relation="proyectos_recursos",column1="proyecto_id",column2="recurso_id",string="Recursos")

    @api.depends('laboratorios_id','prioridad')
    def _get_titulo(self):
        for proyecto in self:
            laboratorios=self.env['iawilliamandres.laboratorio'].search([('proyectos_id','=',proyecto.id)])
            for laboratorio in laboratorios:
                if laboratorio==None:
                    proyecto.titulo="No ubicacion"
                else:
                    proyecto.titulo=laboratorio.nombre
        
        if proyecto.prioridad>7:
            proyecto.titulo+="Urgente"
        else:
            proyecto.titulo+="Proridad: "+str(proyecto.prioridad)

    @api.depends('prioridad')
    def _get_prioridad(self):
            if self.prioridad > 7:
                self.urgente=True
            else:
                self.urgente=False

    @api.constrains('prioridad')
    def _check_prioridad(self):
        if self.prioridad>10:
            raise ValidationError("La prioridad no puede ser superior a 10")
    
        

