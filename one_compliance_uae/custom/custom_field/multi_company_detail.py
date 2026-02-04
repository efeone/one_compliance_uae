def get_multi_company_detail_custom_fields():
	'''
	Custom fields that need to be added to the Multi Company Detail Doctype
	'''
	return {
		"Multi Company Detail": [
			{
				"fieldname": "licensing_authority",
				"fieldtype": "Link",
				"label": "Licensing Authority",
				"options": "Licensing Authority",
                "in_list_view": 1,
				"insert_after": "company_name"
			}
        ]
    }