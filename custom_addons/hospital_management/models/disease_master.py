from odoo import models, fields


class disease_master(models.Model):
    _name = 'hospital_management.disease_master'
    _description = 'hospital_management.disease_master'

    code = fields.Float(string="Code")
    name = fields.Char(string="Name")
