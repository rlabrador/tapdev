# -*- coding: utf-8 -*-
from openerp import http

class Tapmain(http.Controller):
    #appel index comme page de template
     @http.route('/tapmain/', auth='public')
     def index(self, **kw):
        Usertests = http.request.env['tapmain.usertest']
        return http.request.render('tapmain.index', {
            'usertests': Usertests.search([])
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