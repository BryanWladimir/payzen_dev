# -*- coding: utf-8 -*-
# from odoo import http


# class Birthdat(http.Controller):
#     @http.route('/birthdat/birthdat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/birthdat/birthdat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('birthdat.listing', {
#             'root': '/birthdat/birthdat',
#             'objects': http.request.env['birthdat.birthdat'].search([]),
#         })

#     @http.route('/birthdat/birthdat/objects/<model("birthdat.birthdat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('birthdat.object', {
#             'object': obj
#         })
