from odoo import fields,models,api

class StockPickingBatch(models.Model):

    _name = 'stock.picking.batch'
    _inherit = 'stock.picking.batch'  

    dock_id = fields.Many2one( 'dock.stock' , string='Dock')
    vehical_id = fields.Many2one('fleet.vehicle',  string='Vehical')
    vehical_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehical Category',)
    weight = fields.Float(compute='_compute_total_weight' )
    volume = fields.Float(compute='_compute_total_weight' )
    sub_volume = fields.Float(compute='_compute_sub_volume' , string='Volume')

    @api.depends('move_line_ids')
    def _compute_total_weight(self):
        for rec in self:
            rec.weight = sum(rec.move_line_ids.product_id.mapped('weight')) / rec.vehical_category_id.max_weight
            rec.volume = sum(rec.move_line_ids.product_id.mapped('volume')) / rec.vehical_category_id.max_volume
          
    @api.depends('picking_ids')
    def _compute_sub_volume(self):
        for rec in self:
            rec.sub_volume = sum(rec.picking_ids.product_id.mapped('volume'))
            

    