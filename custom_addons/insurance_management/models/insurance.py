# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Insurance(models.Model):
    _name = 'insurance'
    _description = 'Insurance'

    name = fields.Char(string="Name")
    customer_ids = fields.Many2one(string="Contact Detail")
    policy_ids = fields.Many2one(string="Email ID")
    agent_ids = fields.Many2one(string="Gender")
    start_date = fields.Date(string="Related User")
    maturity_date = fields.Date(string="Commission Type")
    premium_paying_perid = fields.Float(string="Amount")
    payment_mode = fields.Float(string="Percentage")
    total_policy_amount = fields.Float(string="Total Commission")
    total_commission_amount = fields.Float(string="Total Commission")
    no_of_premium = fields.One2many()
    number = fields.One2many()
    due_date = fields.One2many()
    premium_amount = fields.One2many()
    commission_amount = fields.One2many()

    # insurance_ids = fields.One2many('', string='Insurance')
    # name = fields.Text(related='patient_name.symptoms', string='Name', readonly=True)
    # customer_id = fields.Many2one(related='patient_name.disease', string='Customer', readonly=True)
    # policy_id = fields.Many2one(related='patient_name.cure_for_disease', string='Policy', readonly=True)
    # amount = fields.float(related='patient_name.medicines', string='Amount', readonly=True)
    # total_commission_amount = fields.float(related='patient_name.medicines', string='Total Commission Amount', readonly=True)
    # state = fields.Selection(related='patient_name.medicines', string='State', readonly=True)
