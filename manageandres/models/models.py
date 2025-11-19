# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class manageandres(models.Model):
#     _name = 'manageandres.manageandres'
#     _description = 'manageandres.manageandres'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class task(models.Model):
    _name='manageandres.task'
    _description='manageandres.task'

    name=fields.Char()
    description=fields.Char()
    star_date=fields.Datetime()
    end_date=fields.Datetime()
    is_paused=fields.Boolean()


class sprint(models.Model):
    _name='manageandres.sprint'
    _description='manageandres.sprint'

    name=fields.Char()
    description=fields.Char()
    start_date=fields.Datetime()
    end_date=fields.Datetime()

class project(models.Model):
    _name='manageandres.project'
    _description='manageandres.project'

    name=fields.Char()
    description=fields.Char()

class history(models.Model):
    _name='manageandres.history'
    _description='manageandres.history'

    name=fields.Char()
    description=fields.Char()

class technology(models.Model):
    _name='manageandres.technology'
    _description='manageandres.technology'

    name=fields.Char()
    description=fields.Char()
    photo=fields.Image()