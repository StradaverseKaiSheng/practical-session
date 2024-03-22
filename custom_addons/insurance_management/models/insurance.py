# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Insurance(models.Model):
    _name = 'insurance'
    _description = 'Insurance'

    name = fields.Char(string="Name")
    customer_ids = fields.Many2one('res.partner', string="Customer")
    policy_ids = fields.Many2one('policy.master', string="Policy")
    agent_ids = fields.Many2one('agent.master', string="Agent")
    start_date = fields.Date(string="Start Date", default=fields.Date.now())
    maturity_date = fields.Date(string="Maturity Date") # computed later
    premium_paying_perid = fields.Integer(related='policy_ids.premium_paying_perid', string="Premium Paying Period (In year)")
    payment_type = fields.Selection(related='policy_ids.payment_type', string="Payment Type")
    payment_mode = fields.Selection(related='policy_ids.payment_mode', string="Payment Mode")
    premium_amount = fields.Float(related='policy_ids.total_policy_amount', string="Premium Amount")
    total_policy_amount = fields.Float(related='policy_ids.total_policy_amount', string="Total Policy Amount")
    total_commission_amount = fields.Float(string="Total Commission Amount") # computed later

    no_of_premium = fields.One2many()
    number = fields.One2many()
    due_date = fields.One2many()
    premium_amount = fields.One2many()
    commission_amount = fields.One2many()
    # state = fields.Selection(related='patient_name.medicines', string='State', readonly=True)

    # insurance_ids = fields.One2many('', string='Insurance')
    # name = fields.Text(related='patient_name.symptoms', string='Name', readonly=True)
    # customer_id = fields.Many2one(related='patient_name.disease', string='Customer', readonly=True)
    # policy_id = fields.Many2one(related='patient_name.cure_for_disease', string='Policy', readonly=True)
    # amount = fields.float(related='patient_name.medicines', string='Amount', readonly=True)
    # total_commission_amount = fields.float(related='patient_name.medicines', string='Total Commission Amount', readonly=True)
    # state = fields.Selection(related='patient_name.medicines', string='State', readonly=True)
