from odoo import fields, models, _, api


class RecruitmentCourse(models.Model):
    _name = 'recruitment.course'
    _description = 'Recruitment course'

    name = fields.Char(string='Name')
    date_from = fields.Datetime(string='From')
    date_to = fields.Datetime(string='To')
    candidate_ids = fields.Many2many(comodel_name='res.partner', string='Candidates')
