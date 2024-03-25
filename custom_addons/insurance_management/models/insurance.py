# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Insurance(models.Model):
    _name = 'insurance'
    _description = 'Insurance'

    name = fields.Char(string="Name", readonly=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    policy_id = fields.Many2one('policy.master', string="Policy")
    agent_id = fields.Many2one('agent.master', string="Agent")
    start_date = fields.Date(string="Start Date", default=fields.Date.today())

    maturity_date = fields.Date(string="Maturity Date", readonly=True) # computed later

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

    def action_confirm(self):
        for record in self:
            self.state = 'confirm'

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


# class NoOfPremium(models.Model):
#     _name = 'noofpremium'
#     _description = 'No of Premium'

#     number_ids = fields.One2many()
#     due_date_ids = fields.One2many()
#     premium_amount_ids = fields.One2many()
#     commission_amount_ids = fields.One2many()

