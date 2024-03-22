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
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('sent_email', 'Sent Email'),
        ('approved', 'Approved'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default="draft", string="State", required=True)

    def action_in_progress(self):
        self.state = 'in_progress'

    def action_sent_email(self):
        self.state = 'sent_email'

    def action_approved(self):
        self.state = 'approved'

    def action_done(self):
        self.state = 'done'

    def action_reset_to_draft(self):
        self.state = 'draft'

    # def action_cancel(self):
    #     return {
    #         'name': 'Cancellation Remark',
    #         'view_mode': 'form',
    #         'view_id': False,
    #         'view_type': 'form',
    #         'res_model': 'hospital_management.cancellation_remark_wizard',
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #     }
