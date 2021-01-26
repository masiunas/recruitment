from odoo import fields, models, _, api

RECRUITMENT_STATE = [
    ('active', 'Active'),
    ('process', 'Process'),
    ('reserve', 'Reserve'),
]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    recruitment_state = fields.Selection(selection=RECRUITMENT_STATE)
