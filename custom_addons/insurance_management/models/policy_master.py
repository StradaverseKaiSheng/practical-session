# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PolicyMaster(models.Model):
    _name = 'policy.master'
    _description = 'Policy Master'

    code = fields.Float(string="Code", readonly=True)
    name = fields.Char(string="Name")
    policy_type = fields.Selection([
        ('life_insurance', 'Life Insurance'),
        ('car_insurance', 'Car Insurance'),
        ('mediclaim', 'Mediclaim')], string="Policy Type")
    premium_paying_period = fields.Integer(string="Premium Paying Period (In year)")
    payment_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('installment', 'Installment')], string="Payment Type")
    payment_mode = fields.Selection([
        ('yearly', 'Yearly'),
        ('half_yearly', 'Half Yearly'),
        ('quarterly', 'Quarterly'),
        ('monthly', 'Monthly')], string="Policy Mode")
    premium_amount = fields.Float(string="Premium Amount")
    total_policy_amount = fields.Float(string="Total Policy Amount", compute='_compute_total_policy_amount', store=True, readonly=True)
    notes = fields.Html(string="Notes")

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('policy.master')
        return super(PolicyMaster, self).create(vals)

    @api.depends('premium_paying_period', 'payment_mode', 'premium_amount')
    def _compute_total_policy_amount(self):
        for record in self:
            if record.payment_type == 'installment':
                if record.payment_mode =='yearly':
                    record.total_policy_amount = record.premium_paying_period * record.premium_amount
                elif record.payment_mode =='half_yearly':
                    record.total_policy_amount = record.premium_paying_period * record.premium_amount * 2
                elif record.payment_mode =='quarterly':
                    record.total_policy_amount = record.premium_paying_period * record.premium_amount * 3
                else:
                    record.total_policy_amount = record.premium_paying_period * record.premium_amount * 12
            else:
                 record.total_policy_amount = record.premium_amount # assume tbc