def get_opportunity_custom_fields():
	'''
	Custom fields that need to be added to the Opportunity Doctype
	'''
	return {
		"Opportunity": [
			{
				"fieldname": "licensing_authority",
				"fieldtype": "Link",
				"label": "Licensing Authority",
				"options": "Licensing Authority",
				"insert_after": "website"
			}
        ]
    }