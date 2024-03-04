{
    'name': "Transport Management Sysytem",
    'version': '0.1',
    'depends': ['stock_picking_batch' , 'fleet' ],
    'license': 'LGPL-3',
    'category': 'Localization',
    'description': """
    Transport Management System
    """,
    'installable': True,
    'application': True,
    'auto_install': False,
    'data' : [
        'security/ir.model.access.csv',
        'views/stock_transport_fleet_category.xml',
        'views/stock_picking_batch_inherit_views.xml'
    ]
}