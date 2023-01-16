# -*- coding: utf-8 -*-
# from odoo import http


# class Indomaret(http.Controller):
#     @http.route('/indomaret/indomaret', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/indomaret/indomaret/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('indomaret.listing', {
#             'root': '/indomaret/indomaret',
#             'objects': http.request.env['indomaret.indomaret'].search([]),
#         })

#     @http.route('/indomaret/indomaret/objects/<model("indomaret.indomaret"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('indomaret.object', {
#             'object': obj
#         })
