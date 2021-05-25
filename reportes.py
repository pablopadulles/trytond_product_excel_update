from trytond.report import Report
from trytond.pool import Pool
from trytond.transaction import Transaction
from PIL import Image, ImageDraw, ImageFont
import qrcode
from io import BytesIO
import urllib
import time
import pytz
from datetime import datetime, timedelta, time



class ReportProductExcelExport(Report):
    'Report ExportarProductos'
    __name__ = 'product.excel.export'

    @classmethod
    def _get_products(cls):
        pool = Pool()
        ProductTemplate = pool.get('product.template')
        return ProductTemplate.search([])

    @classmethod
    def get_context(cls, records, data):
        report_context = super(ReportProductExcelExport, cls).get_context(records, data)
        report_context['templates'] = cls._get_products()
        return report_context
