# -*- coding: utf-8 -*-
#############################################################################
# (c) 2015 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See LICENSE file on root folder for details
#############################################################################

{
    "name": "Prevent the automatic creation of the variants of a product",
    "summary": "Disable automatic product variant creation",
    "version": "1.0",
    "category": "Product Management",
    "license": "AGPL-3",
    "author": "OdooMRP team, "
              "AvanzOSC, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Odoo Community Association (OCA)",
    "website": "http://www.odoomrp.com",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
    ],
    "depends": [
        "product",
    ],
    "data": [
        "views/product_view.xml",
    ],
    "installable": True,
}
