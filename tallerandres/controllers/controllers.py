# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class vehiculo_controller(http.Controller):
    @http.route('/api/vehiculos', auth='public',method=['GET'], csrf=False)
    def get_vehiculos(self,**kw):
        try:
            vehiculos=http.request.env['tallerandres.vehiculo'].sudo().search_read([],['name','id_marca','modelo'])
            res=json.dumps(vehiculos,ensure_ascii=False).encode('utf-8')
            return Response(res,content_type='application/json;charset=utf-8',status=200)
        except Exception as e:
            return Response(json.dumps({'error':str(e)}),content_type='application/json;charset=utf-8',status=505)
     

    

