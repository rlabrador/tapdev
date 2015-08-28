# -*- coding: utf-8 -*-
from openerp import http

class Tapmain(http.Controller):
    #appel index comme page de template
     @http.route('/tapmain/', auth='public', website=True)
     def index(self, **kw):
        Contractors = http.request.env['tapmain.contractor']
        return http.request.render('tapmain.index', {
            'contractors': Contractors.search([])
        })

#     @http.route('/tapmain/tapmain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tapmain.listing', {
#             'root': '/tapmain/tapmain',
#             'objects': http.request.env['tapmain.tapmain'].search([]),
#         })

#     @http.route('/tapmain/tapmain/objects/<model("tapmain.tapmain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tapmain.object', {
#             'object': obj
#         })