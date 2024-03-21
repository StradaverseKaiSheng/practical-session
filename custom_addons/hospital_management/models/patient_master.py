from odoo import models, fields


class patient_master(models.Model):
    _name = 'hospital_management.patient_master'
    _description = 'hospital_management.patient_master'

    date = fields.Datetime(string="Date", default=fields.Datetime.now())
    name = fields.Char(string="Name")
    gender = fields.Selection([
                ('male', 'Male'),
                ('female', 'Female')], string="Gender")
    age = fields.Float(string="Age")
    mobile = fields.Float(string="Mobile")
    symptoms = fields.Text(string="Symptoms", required=True)
    disease = fields.Many2many('hospital_management.disease_master', relation='disease_patient_rel', string='Disease', required=True)
    cure_for_disease = fields.Text(string="Cure for Disease", required=True)
    medicines = fields.Text(string="Medicines", required=True)
    cancellation_remark = fields.Text(string="Cancellation Remark")
