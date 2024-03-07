from odoo import models,fields,api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float(string="Volume", compute='_compute_volume')
    
    @api.depends('move_ids.product_id.volume', 'move_ids.quantity')
    def _compute_volume(self):
        for picking in self:
            picking_volume = sum(line.product_id.volume * line.quantity for line in picking.move_ids)
            picking.volume = picking_volume