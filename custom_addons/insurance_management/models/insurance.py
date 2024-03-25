# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Insurance(models.Model):
    _name = 'insurance'
    _description = 'Insurance'

    name = fields.Char(string="Name", readonly=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    policy_id = fields.Many2one('policy.master', string="Policy")
    agent_id = fields.Many2one('agent.master', string="Agent")
    start_date = fields.Date(string="Start Date", default=fields.Date.today())
    maturity_date = fields.Date(string="Maturity Date", compute='_compute_maturity_date', store=True, readonly=True)
    premium_paying_period = fields.Integer(related='policy_id.premium_paying_period', string="Premium Paying Period (In year)", readonly=True)
    payment_type = fields.Selection(related='policy_id.payment_type', string="Payment Type", readonly=True)
    payment_mode = fields.Selection(related='policy_id.payment_mode', string="Payment Mode", readonly=True)
    premium_amount = fields.Float(related='policy_id.premium_amount', string="Premium Amount", readonly=True)
    total_policy_amount = fields.Float(related='policy_id.total_policy_amount', string="Total Policy Amount", readonly=True)
    
    total_commission_amount = fields.Float(string="Total Commission Amount", readonly=True) # computed later

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('sent_email', 'Sent Email'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default="draft", string="State", required=True)
    no_of_premium_ids = fields.One2many('no.of.premium', 'insurance_id', string="No of Premium")

    def action_confirm(self):
        for record in self:
            self.state = 'confirm'

            if record.payment_mode == 'yearly':
                number_of_premium = record.premium_paying_period
            elif record.payment_mode == 'half_yearly':
                number_of_premium = record.premium_paying_period * 2
            elif record.payment_mode == 'quarterly':
                number_of_premium = record.premium_paying_period * 4
            elif record.payment_mode == 'monthly':
                number_of_premium = record.premium_paying_period * 12

            current_date = fields.Date.from_string(record.start_date)
            no_of_premium_list = []
            for _ in range(number_of_premium):
                commission_amount = 0
                if record.agent_id.commission_type == 'fixed':
                    commission_amount = record.agent_id.amount
                elif record.agent_id.commission_type == 'based_on_percentage':
                    commission_amount = (record.agent_id.percentage / 100) * record.total_policy_amount

                no_of_premium_list.append({
                    'insurance_id': record.id,
                    'due_date': current_date,
                    'premium_amount': record.premium_amount,
                    'commission_amount': commission_amount
                })

                if record.payment_mode == 'yearly':
                    current_date += timedelta(days=365) # Assume
                elif record.payment_mode == 'half_yearly':
                    current_date += timedelta(days=180) # Assume
                elif record.payment_mode == 'quarterly':
                    current_date += timedelta(days=90) # Assume
                elif record.payment_mode == 'monthly':
                    current_date += timedelta(days=30) # Assume

            NoOfPremium = self.env['no.of.premium']
            for i in range(no_of_premium_list):
                NoOfPremium.create(i)

    def action_sent_email(self):
        for record in self:
            self.state = 'sent_email'
            
    def action_done(self):
        for record in self:
            self.state = 'done'

    def action_cancel(self):
        for record in self:
            self.state = 'cancel'

    def action_reset_to_draft(self):
        for record in self:
            self.state = 'draft'

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('insurance')
        return super(Insurance, self).create(vals)
    
    @api.depends('start_date', 'premium_paying_period')
    def _compute_maturity_date(self):
        for record in self:
            record.maturity_date = fields.Date.from_string(record.start_date) + timedelta(days=365 * record.premium_paying_period)


class NoOfPremium(models.Model):
    _name = 'no.of.premium'
    _description = 'No of Premium'

    insurance_id = fields.Many2one('insurance', string="Insurance")
    number = fields.Char(string="Number")
    due_date = fields.Date(string="Due Date")
    premium_amount = fields.Float(string="Premium Amount")
    commission_amount = fields.Float(string="Commission Amount")

    @api.model
    def create(self, vals):
        vals['number'] = self.env['ir.sequence'].next_by_code('no.of.premium')
        return super(NoOfPremium, self).create(vals)
