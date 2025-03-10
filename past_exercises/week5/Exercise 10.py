sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

products = ["ITEM-453","ITEM-324","ITEM-432","ITEM-23"]

result = {
	'ITEM-453': 0,
	'ITEM-324': 0,
	'ITEM-432': 0,
	'ITEM-23': 0,
}

for key_final_result , value_final_result in result.items():

    for key_sales_list in range(0,len(sales)):
       
        for key_item_list, value in enumerate(sales[key_sales_list]["items"]):
           
            if (sales[key_sales_list]["items"][key_item_list]["upc"]==key_final_result):

                result[sales[key_sales_list]["items"][key_item_list]["upc"] ] = result[sales[key_sales_list]["items"][key_item_list]["upc"]] + sales[key_sales_list]["items"][key_item_list]["unit_price"]


print ("The total sales for each UPC is: ")
print (result)
