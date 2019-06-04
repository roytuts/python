import datetime
import xlrd
from xlrd import open_workbook

class OrderDetails(object):

    def __init__(self, order_date, region, rep, item, units, unit_cost, total):
        self.order_date = order_date
        self.region = region
        self.rep = rep
        self.item = item
        self.units = units
        self.unit_cost = unit_cost
        self.total = total
		
    def __str__(self):
        return("Order details:\n"
            "  Order Date = {0}\n"
            "  Region = {1}\n"
            "  Representative = {2}\n"
            "  Item = {3}\n"
            "  Units = {4} \n"
            "  Unit Cost = {5} \n"
            "  Total = {6} \n"
            .format(self.order_date, self.region, self.rep, self.item, self.units, self.unit_cost, self.total))
			
wb = open_workbook('OrderData.xlsx')

for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    items = []
    rows = []
                
    #skip the first row as it contains headers
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            if(sheet.cell_type(row,col) == 3):
                value  = (sheet.cell(row,col).value)
                try:
                    value = datetime.datetime(* (xlrd.xldate_as_tuple(sheet.cell(row,col).value, wb.datemode))).strftime('%d.%m.%Y')
                except ValueError:
                    pass
                finally:
                    values.append(value)
            else:
                value  = (sheet.cell(row,col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
        item = OrderDetails(*values)
        items.append(item)
		
for item in items:
    print(item)
    print("Accessing single attribut's value (eg. Order Date): {0}\n".format(item.order_date))
    print