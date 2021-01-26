from odoo import fields, models, _, api

EVENT_TYPE = [
    ('call', 'Call'),
    ('interview', 'Interview'),
]


class RecruitmentEvent(models.Model):
    _name = 'recruitment.event'
    _description = 'Recruitment event'
    _order = 'event_date'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Candidate')
    partner_image = fields.Binary(related='partner_id.image_1920')
    event_type = fields.Selection(selection=EVENT_TYPE, string='Type')
    event_date = fields.Datetime(string='Date', default=fields.Datetime.now())
    event_note = fields.Text(string='Note')
    event_responsible = fields.Many2one(comodel_name='res.users', string='Responsible',
                                        default=lambda self: self.env.user)
    display_name = fields.Char(compute='_compute_display_name', store=True)
    is_done = fields.Boolean(string='Done')

    @api.depends
    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.event_type} to {record.partner_id.name}.'

    def action_done(self):
        self.write({'is_done': True, })
