# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class project_controller(http.Controller):
    @http.route('/api/projects',auth='public',method=['GET'],csrf=False)
    def get_projects(self,**kw):
        try:
            projects=http.request.env['manageandres.project'].sudo().search_read([],['name','description'])
            res=json.dumps(projects,ensure_ascii=False).encode('utf-8')
            return Response(res,content_type='application/json:charset=utf-8',status=200)
        except Exception as e:
            return Response(json.dumps({'error':str(e)}),content_type='application/json;charset=utf-8',status=505)

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

