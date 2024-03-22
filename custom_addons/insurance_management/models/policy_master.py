# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PolicyMaster(models.Model):
    _name = 'policy.master'
    _description = 'Policy Master'

    code = fields.Float(string="Code")
    name = fields.Char(string="Name")
    policy_type = fields.Selection([
        ('life_insurance', 'Life Insurance'),
        ('car_insurance', 'Car Insurance'),
        ('mediclaim', 'Mediclaim')], string="Policy Type")
    premium_paying_period = fields.Integer(string="Premium Paying Period")
    payment_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('installment', 'Installment')], string="Payment Type")
    payment_mode = fields.Selection([
        ('yearly', 'Yearly'),
        ('half_yearly', 'Half Yearly'),
        ('quarterly', 'Quarterly'),
        ('monthly', 'Monthly')], string="Policy Mode")
    premium_amount = fields.Float(string="Premium Amount")
    total_policy_amount = fields.Float(string="Total Policy Amount")
    notes = fields.Html(string="Notes")

    # @api.depends('premium_paying_period', 'payment_mode', 'premium_amount')
    # def _compute_total_policy_amount(self):
    #     for record in self:
    #         record.total_policy_amount = record.field1 + record.field2
