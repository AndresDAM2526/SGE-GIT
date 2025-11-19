# -*- coding: utf-8 -*-
# from odoo import http


# class Manageandres(http.Controller):
#     @http.route('/manageandres/manageandres', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageandres/manageandres/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageandres.listing', {
#             'root': '/manageandres/manageandres',
#             'objects': http.request.env['manageandres.manageandres'].search([]),
#         })

#     @http.route('/manageandres/manageandres/objects/<model("manageandres.manageandres"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageandres.object', {
#             'object': obj
#         })

