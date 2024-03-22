# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PolicyMaster(models.Model):
    _name = 'policy.master'
    _description = 'Policy Master'

    code = fields.Float(string="Code")
    name = fields.Char(string="Name")
    contact_detail = fields.Float(string="Contact Detail")
    email_id = fields.Char(string="Email ID")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')], string="Gender")
    related_user_ids = fields.Many2one('res_users', string="Related User")
    commission_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('based_on_percentage', 'Based on Percentage')], string="Commission Type")
    amount = fields.Float(string="Amount")
    percentage = fields.Float(string="Percentage")
    total_commission = fields.Float(string="Total Commission")

    # insurance_ids = fields.One2many('', string='Insurance')
    # name = fields.Text(related='patient_name.symptoms', string='Name', readonly=True)
    # customer_id = fields.Many2one(related='patient_name.disease', string='Customer', readonly=True)
    # policy_id = fields.Many2one(related='patient_name.cure_for_disease', string='Policy', readonly=True)
    # amount = fields.float(related='patient_name.medicines', string='Amount', readonly=True)
    # total_commission_amount = fields.float(related='patient_name.medicines', string='Total Commission Amount', readonly=True)
    # state = fields.Selection(related='patient_name.medicines', string='State', readonly=True)
