from odoo import fields,models,api

class FleetVehicleModelCategory(models.Model):

    _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Integer(string="Max Weight(kg)" , default=1)
    max_volume = fields.Integer(string="Max Volume", default=1)
    display_name = fields.Char()

    @api.depends('name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.max_weight}kg , {rec.max_volume}m3)"