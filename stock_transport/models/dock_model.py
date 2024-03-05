from odoo import fields,models

class DockModel(models.Model):
    _name = 'dock.model'
    _description = 'Dock Stock'

    name = fields.Char(string='Name')