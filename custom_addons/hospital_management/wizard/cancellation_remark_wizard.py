from odoo import models, fields

class CancelPatientWizard(models.TransientModel):
    _name = 'hospital_management.cancellation_remark_wizard'
    _description = 'Cancellation Remark Wizard'

    cancellation_remark = fields.Text(string="Cancellation Remark")

    def confirm_cancelation(self):
        active_id = self._context.get('active_id')
        if active_id:
            patient_record = self.env['hospital_management.patient_master'].browse(active_id)
            patient_record.write({'state': 'draft', 'cancellation_remark': self.cancellation_remark})
        return {'type': 'ir.actions.act_window_close'}
