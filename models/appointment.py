from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _rec_name = 'patient_id'

    reference = fields.Char(
        string="Reference No", 
        default='New')
    date = fields.Datetime(
        string='Date'
        )
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor Name'
    )
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient Name'
    )
    gender = fields.Selection(
        [('male', 'Male'), 
         ('female', 'Female')],
        string='Patient Gender',
        related='patient_id.gender',
        readonly=True
    )

    @api.model
    def create(self, vals):
        if vals.get('reference') in [False, 'New']:
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'New'
        return super(Appointment, self).create(vals)
