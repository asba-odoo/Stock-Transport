from odoo import fields,models

class DockStock(models.Model):
    _name = 'dock.stock'
    _description = 'Dock Stock'

    name = fields.Char(string='Name')