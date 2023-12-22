# -*- coding: utf-8 -*-
from odoo import api, fields, models

class FamiliaM(models.Model):
    _name = 'familia.m'
    name = fields.Char(string='name', required=True)
    last_name = fields.Char(string='last_name', required=True)
    age = fields.Integer(string='age')
    relationship = fields.Selection([('father', 'Father'),
                             ('son', 'Son'),
                             ('grandson', 'Grandson'),
                             ("user", "User"),
                             ("couple","Couple")], string='relationship', default="user", required=True)