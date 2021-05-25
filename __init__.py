# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import reportes
from . import wizard

def register():
    Pool.register(
        wizard.ActualizarProductosView,
        module='product_excel_update', type_='model')
    Pool.register(
        reportes.ReportProductExcelExport,
        module='product_excel_update', type_='report')
    Pool.register(
        wizard.ActualizarProductosWizard,
        module='product_excel_update', type_='wizard')