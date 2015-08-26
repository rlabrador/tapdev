# -*- coding: utf-8 -*-
from openerp import http

# class Tapmain(http.Controller):
#     @http.route('/tapmain/tapmain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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