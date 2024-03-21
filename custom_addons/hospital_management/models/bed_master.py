from odoo import models, fields


class bed_master(models.Model):
    _name = 'hospital_management.bed_master'
    _description = 'hospital_management.bed_master'

    bed_number = fields.Float(string="Bed Number")
    bed_type = fields.Selection([
                ('icu', 'ICU Bed'),
                ('special', 'Special Bed'),
                ('semi_special', 'Semi Special Bed'),
                ('normal', 'Normal Bed')], string="Bed Type")
