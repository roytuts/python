import xlwt

class OrderDetail(object):

    def __init__(self, order_date, region, rep, item, units, unit_cost, total):
        self.order_date = order_date
        self.region = region
        self.rep = rep
        self.item = item
        self.units = units
        self.unit_cost = unit_cost
        self.total = total

def write_to_excel(filename, sheet, odList):
	book = xlwt.Workbook()
	sh = book.add_sheet(sheet)
	
	#total items
	total_items = len(odList)
	print("total_items: ", total_items)
	
	#print on console
	for od in odList:
		print(od.order_date)
		print(od.region)
		print(od.rep)
		print(od.item)
		print(od.units)
		print(od.unit_cost)
		print(od.total)
		print('\n')
	
	#write headers
	sh.write(0, 0, 'OrderDate')
	sh.write(0, 1, 'Region')
	sh.write(0, 2, 'rep')
	sh.write(0, 3, 'Item')
	sh.write(0, 4, 'Units')
	sh.write(0, 5, 'Unit Cost')
	sh.write(0, 6, 'Total')
	
	#write row values
	for idx in range(len(odList)):
		#print(idx)
		sh.write(idx+1, 0, odList[idx].order_date)
		sh.write(idx+1, 1, odList[idx].region)
		sh.write(idx+1, 2, odList[idx].rep)
		sh.write(idx+1, 3, odList[idx].item)
		sh.write(idx+1, 4, odList[idx].units)
		sh.write(idx+1, 5, odList[idx].unit_cost)
		sh.write(idx+1, 6, odList[idx].total)	
		
	book.save(filename)

od1 = OrderDetail('2016-1-6', 'East', 'Jones', 'Pencil', 95, 1.99, 189.05)
od2 = OrderDetail('2016-1-23', 'Central', 'Kivell', 'Binder', 50, 19.99, 999.50)
od3 = OrderDetail('2016-2-9', 'Central', 'Jardine', 'Pencil', 36, 4.99, 179.64)
od4 = OrderDetail('2016-2-26', 'Central', 'Gill', 'Pen', 27, 19.99, 539.73)

odList = [od1, od2, od3, od4]

write_to_excel('OrderDetails.xls', 'Sheet1', odList)