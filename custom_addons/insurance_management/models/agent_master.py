# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AgentMaster(models.Model):
    _name = 'agent.master'
    _description = 'Agent Master'

    code = fields.Float(string="Code")
    name = fields.Char(string="Name", required=True)
    contact_detail = fields.Float(string="Contact Detail")
    email_id = fields.Char(string="Email ID")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')], string="Gender")
    related_user_ids = fields.Many2one('res.users', string="Related User")
    commission_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('based_on_percentage', 'Based on Percentage')], string="Commission Type")
    amount = fields.Float(string="Amount")
    percentage = fields.Float(string="Percentage")
    total_commission = fields.Float(string="Total Commission")
    insurance_id = fields.One2many('insurance', string='Insurance')
    name = fields.Text(related='insurance.name', string='Name', readonly=True)
    customer_ids = fields.Many2one(related='insurance.customer_ids', string='Customer', readonly=True)
    policy_ids = fields.Many2one(related='insurance.policy_ids', string='Policy', readonly=True)
    amount = fields.float(related='insurance.amount', string='Amount', readonly=True)
    total_commission_amount = fields.float(related='insurance.total_commission_amount', string='Total Commission Amount', readonly=True)
    state = fields.Selection(related='insurance.state', string='State', readonly=True)

    # @api.depends('premium_paying_period', 'payment_mode', 'premium_amount')
    # def _compute_total_commission(self):
    #     for record in self:
    #         if record.payment_type == 'installment':
    #             if record.payment_mode =='yearly':
    #                 record.total_policy_amount = record.premium_paying_period * record.premium_amount
    #             elif record.payment_mode =='half_yearly':
    #                 record.total_policy_amount = record.premium_paying_period * record.premium_amount * 2
    #             elif record.payment_mode =='quarterly':
    #                 record.total_policy_amount = record.premium_paying_period * record.premium_amount * 3
    #             else:
    #                 record.total_policy_amount = record.premium_paying_period * record.premium_amount * 12
    #         else:
    #             # temp
    #              record.total_policy_amount = record.premium_paying_period * record.premium_amount
