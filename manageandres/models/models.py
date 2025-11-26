# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class task(models.Model):
    _name='manageandres.task'
    _description='manageandres.task'

    project=fields.Many2one("manageandres.project",related="history_id.project_id",readonly=True)
    code=fields.Char(compute="_get_code", store=False)
    name=fields.Char()
    description=fields.Char()
    start_date=fields.Datetime()
    end_date=fields.Datetime()
    is_paused=fields.Boolean()

    history_id=fields.Many2one("manageandres.history",string="History", required=True,ondelete="cascade")
    sprint=fields.Many2one("manageandres.sprint",compute="_get_sprint",store=True)
    technologies_id=fields.Many2many(comodel_name="manageandres.technology",relation="sprint_task",column1="technology_id",column2="task_id",string="Technologies")

    def _get_code(self):
        for task in self:
            task.code="TSK_"+str(task.id)
    
    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints=self.env['manageandres.sprint'].search([('project_id','=',task.history_id.project_id.id)])
            found=False
            for sprint in sprints:
                if isinstance(sprint.end_date,datetime.datetime) and sprint.end_date>datetime.datetime.now():
                    task.sprint=sprint.id
                    found=True
            if not found:
                task.sprint=False

    

class sprint(models.Model):
    _name='manageandres.sprint'
    _description='manageandres.sprint'

    name=fields.Char()
    description=fields.Char()
    start_date=fields.Datetime()
    duration=fields.Integer()
    end_date=fields.Datetime(compute="_get_end_date",store=True)
    

    tasks_id=fields.One2many(string="Tasks",comodel_name="manageandres.task",inverse_name="sprint")
    project_id=fields.Many2one("manageandres.project",string="Project",required=True,ondelete="cascade")

    @api.depends('start_date','duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date,datetime.datetime) and sprint.duration>0:
                sprint.end_date=sprint.start_date+datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date=sprint.start_date
    

class project(models.Model):
    _name='manageandres.project'
    _description='manageandres.project'

    name=fields.Char()
    description=fields.Char()

    histories_id=fields.One2many(string="Histories",comodel_name="manageandres.history",inverse_name="project_id")
    sprints_id=fields.One2many(string="Sprints",comodel_name="manageandres.sprint",inverse_name="project_id")



class history(models.Model):
    _name='manageandres.history'
    _description='manageandres.history'

    name=fields.Char()
    description=fields.Char()

    project_id=fields.Many2one("manageandres.project",string="Project",required=True,ondelete="cascade")
    tasks_id=fields.One2many(string="Tasks",comodel_name="manageandres.task",inverse_name="history_id")
    used_technologies=fields.Many2many("manageandres.technology",compute="_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies=None
            for task in history.tasks_id:
                if not technologies:
                    technologies=task.technologies_id
                else:
                    technologies=technologies+task.technologies_id
            history.used_technologies=technologies


class technology(models.Model):
    _name='manageandres.technology'
    _description='manageandres.technology'

    name=fields.Char()
    description=fields.Char()
    photo=fields.Image()

    tasks_id=fields.Many2many(comodel_name="manageandres.task",relation="sprint_task",column1="task_id",column2="technology_id",string="Tasks")