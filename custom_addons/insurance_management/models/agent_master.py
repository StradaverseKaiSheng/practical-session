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
    related_user_id = fields.Many2one('res.users', string="Related User")
    commission_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('based_on_percentage', 'Based on Percentage')], string="Commission Type")
    amount = fields.Float(string="Amount")
    percentage = fields.Float(string="Percentage")
    total_commission = fields.Float(string="Total Commission")
    insurance_ids = fields.One2many('insurance', 'agent_id', string="Insurance")
