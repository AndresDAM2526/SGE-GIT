# -*- coding: utf-8 -*-
# from odoo import http


# class Tallerandres(http.Controller):
#     @http.route('/tallerandres/tallerandres', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tallerandres/tallerandres/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tallerandres.listing', {
#             'root': '/tallerandres/tallerandres',
#             'objects': http.request.env['tallerandres.tallerandres'].search([]),
#         })

#     @http.route('/tallerandres/tallerandres/objects/<model("tallerandres.tallerandres"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tallerandres.object', {
#             'object': obj
#         })

