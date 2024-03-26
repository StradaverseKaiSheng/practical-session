from odoo import models, fields, api
from odoo.exceptions import ValidationError


class bed_allocation(models.Model):
    _name = 'hospital_management.bed_allocation'
    _description = 'hospital_management.bed_allocation'

    date = fields.Datetime(string="Date", default=fields.Datetime.now())
    patient_name = fields.Many2one('hospital_management.patient_master', string='Patient')
    symptoms = fields.Text(related='patient_name.symptoms', string='Symptoms', readonly=True)
    disease = fields.Many2many('hospital_management.disease_master', related='patient_name.disease', string='Disease', readonly=True)
    cure_for_disease = fields.Text(related='patient_name.cure_for_disease', string='Cure for Disease', readonly=True)
    medicines = fields.Text(related='patient_name.medicines', string='Medicines', readonly=True)
    bed_type = fields.Many2one('hospital_management.bed_master', string='Bed Type')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('bed_allocated', 'Bed Allocated'),
        ('discharge', 'Discharge'),
        ('cancel', 'Cancel')
    ], default="draft", string="State", required=True)

    def action_bed_allocated(self):
        self.state = 'bed_allocated'

    def action_discharge(self):
        self.state = 'discharge'

    def action_cancel(self):
        self.state = 'cancel'

    @api.onchange('patient_name')
    def onchange_patient_name(self):
        if self.patient_name:
            self.symptoms = self.patient_name.symptoms
            self.disease = self.patient_name.disease
            self.cure_for_disease = self.patient_name.cure_for_disease
            self.medicines = self.patient_name.medicines

    @api.constrains('bed_type')
    def check_bed_availability(self):
        for allocation in self:
            bed_type = allocation.bed_type
            allocated_beds = self.env['hospital_management.bed_allocation'].search_count([('bed_type', '=', bed_type.id), ('state', '=', 'bed_allocated')])
            if allocated_beds > bed_type.bed_number:
                raise ValidationError("No more beds of type '{}' available.".format(bed_type.bed_type))
