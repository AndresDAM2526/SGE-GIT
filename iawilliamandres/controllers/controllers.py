# -*- coding: utf-8 -*-
# from odoo import http


# class Iawilliamandres(http.Controller):
#     @http.route('/iawilliamandres/iawilliamandres', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iawilliamandres/iawilliamandres/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('iawilliamandres.listing', {
#             'root': '/iawilliamandres/iawilliamandres',
#             'objects': http.request.env['iawilliamandres.iawilliamandres'].search([]),
#         })

#     @http.route('/iawilliamandres/iawilliamandres/objects/<model("iawilliamandres.iawilliamandres"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iawilliamandres.object', {
#             'object': obj
#         })

