# -*- coding: utf-8 -*-
from odoo import models, fields, api


class task(models.Model):
    _name='manageandres.task'
    _description='manageandres.task'

    name=fields.Char()
    description=fields.Char()
    start_date=fields.Datetime()
    end_date=fields.Datetime()
    is_paused=fields.Boolean()

    history_id=fields.Many2one("manageandres.history",string="History", required=True,ondelete="cascade")
    sprint_id=fields.Many2one("manageandres.sprint",string="Sprint",required=True,ondelete="cascade")
    technologies_id=fields.Many2many(comodel_name="manageandres.technology",relation="sprint_task",column1="technology_id",column2="task_id",string="Technologies")


class sprint(models.Model):
    _name='manageandres.sprint'
    _description='manageandres.sprint'

    name=fields.Char()
    description=fields.Char()
    start_date=fields.Datetime()
    end_date=fields.Datetime()

    tasks_id=fields.One2many(string="Tasks",comodel_name="manageandres.task",inverse_name="sprint_id")
    project_id=fields.Many2one("manageandres.project",string="Project",required=True,ondelete="cascade")
    

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

class technology(models.Model):
    _name='manageandres.technology'
    _description='manageandres.technology'

    name=fields.Char()
    description=fields.Char()
    photo=fields.Image()

    tasks_id=fields.Many2many(comodel_name="manageandres.task",relation="sprint_task",column1="task_id",column2="technology_id",string="Tasks")