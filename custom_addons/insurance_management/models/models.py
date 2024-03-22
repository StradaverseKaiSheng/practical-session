# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class insurance_management(models.Model):
#     _name = 'insurance_management.insurance_management'
#     _description = 'insurance_management.insurance_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
