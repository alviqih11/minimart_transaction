# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_sale_inherit(models.Model):
#     _name = 'website_sale_inherit.website_sale_inherit'
#     _description = 'website_sale_inherit.website_sale_inherit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
