def get_opportunity_item_custom_fields():
	'''
	Custom fields that need to be added to the Opportunity Item Doctype
	'''
	return {
		"Opportunity Item": [
			{
				"fieldname": "for_the_period",
				"fieldtype": "Data",
				"label": "For the Period",
                "in_list_view": 1,
				"insert_after": "remarks"
			}
        ]
    }