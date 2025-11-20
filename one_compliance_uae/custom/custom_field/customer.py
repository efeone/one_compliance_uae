def get_customer_custom_fields():
	'''
	Custom fields that need to be added to the Customer Doctype
	'''
	return {
		"Customer": [
			{
				"fieldname": "client_acquired_in_the_year",
				"fieldtype": "Date",
				"label": "Client Acquired in the year",
				"insert_after": "aml_compliance_checked"
			},
			{
				"fieldname": "legal",
				"fieldtype": "Tab Break",
				"label": "Legal",
				"reqd": 0,
				"in_list_view": 0,
				"options": "portal_users",
				"depends_on": "",
				"insert_after": "custom_invoice_due_days"
			},
			{
				"fieldname": "licensing_authority",
				"fieldtype": "Data",
				"label": "Licensing Authority",
				"reqd": 0,
				"in_list_view": 0,
				"options": "licensing_authority",
				"depends_on": "",
				"insert_after": "legal"
			},
			{
				"fieldname": "legal_status",
				"fieldtype": "Data",
				"label": "Legal Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "legal_status",
				"depends_on": "",
				"insert_after": "licensing_authority"
			},
			{
				"fieldname": "license_registration_number",
				"fieldtype": "Data",
				"label": "License/Registration Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "license_registration_number",
				"depends_on": "",
				"insert_after": "legal_status"
			},
			{
				"fieldname": "license_issue_date",
				"fieldtype": "Date",
				"label": "License Issue date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "custom_column_break_aay8e"
			},
			{
				"fieldname": "license_expiry_date",
				"fieldtype": "Date",
				"label": "License Expiry date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "license_issue_date"
			},
			{
				"fieldname": "incorporation_registration_date",
				"fieldtype": "Date",
				"label": "Incorporation / Registration date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "license_expiry_date"
			},
			{
				"fieldname": "moa_signing_date",
				"fieldtype": "Date",
				"label": "MOA signing date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "incorporation_registration_date"
			},
			{
				"fieldname": "licensed_business_activity",
				"fieldtype": "Small Text",
				"label": "Licensed Business Activity",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "registered_email_id_with_authority"
			},
			{
				"fieldname": "actual_business_activity",
				"fieldtype": "Small Text",
				"label": "Actual Business Activity",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "moa_signing_date"
			},
			{
				"fieldname": "legal_column_break",
				"fieldtype": "Column Break",
				"insert_after": "actual_business_activity"
			},
			{
				"fieldname": "dubai_chamber_membership_number",
				"fieldtype": "Data",
				"label": "Dubai Chamber Membership Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "custom_dubai_chamber_membership"
			},
			{
				"fieldname": "chamber_membership_start_date",
				"fieldtype": "Date",
				"label": "Chamber Membership Start Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "establishment_card_issue_date"
			},
			{
				"fieldname": "establishment_card_issue_date",
				"fieldtype": "Date",
				"label": "Establishment card issue date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "custom_column_break_eobi8"
			},
			{
				"fieldname": "establishment_card_holder_name",
				"fieldtype": "Data",
				"label": "Establishment card holder name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "dubai_chamber_membership_number"
			},
			{
				"fieldname": "establishment_card_expiry_date",
				"fieldtype": "Date",
				"label": "Establishment card Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "establishment_card_holder_name"
			},
			{
				"fieldname": "registered_mobile_no_with_authority",
				"fieldtype": "Phone",
				"label": "Registered Mobile No (with Authority)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "license_registration_number"
			},
			{
				"fieldname": "registered_email_id_with_authority",
				"fieldtype": "Data",
				"label": "Registered Email ID (with Authority)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "registered_mobile_no_with_authority"
			},
			{
				"fieldname": "license_manager_name",
				"fieldtype": "Data",
				"label": "License Manager Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "legal_column_break"
			},
			{
				"fieldname": "license_manager_email",
				"fieldtype": "Data",
				"label": "License Manager Email",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "license_manager_name"
			},
			{
				"fieldname": "external_authority_permit_",
				"fieldtype": "Data",
				"label": "External Authority Permit",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "license_manager_email"
			},
			{
				"fieldname": "external_authority_name",
				"fieldtype": "Data",
				"label": "External Authority Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "external_authority_permit_"
			},
			{
				"fieldname": "external_authority_permit_expiry_date",
				"fieldtype": "Date",
				"label": "External Authority Permit Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "external_authority_name"
			},
			{
				"fieldname": "company_risk_category",
				"fieldtype": "Data",
				"label": "Company Risk Category",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "trade_name"
			},
			{
				"fieldname": "aml_risk_status",
				"fieldtype": "Data",
				"label": "AML Risk Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"description": "Add AML Status",
				"insert_after": "company_risk_category"
			},
			{
				"fieldname": "aml_column_break",
				"fieldtype": "Column Break",
				"insert_after": "aml_risk_status"
			},
			{
				"fieldname": "mohre_record",
				"fieldtype": "Tab Break",
				"label": "MOHRE Record",
				"reqd": 0,
				"in_list_view": 0,
				"options": "mohre_record",
				"depends_on": "",
				"insert_after": "chamber_membership_start_date"
			},
			{
				"fieldname": "mohre_information",
				"fieldtype": "Section Break",
				"label": "MOHRE Information",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "mohre_record"
			},
			{
				"fieldname": "no_of_employee_quota",
				"fieldtype": "Data",
				"label": "No of Employee Quota (Ministry of Labor/Licensing Authority)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "no_of_employee_quota",
				"depends_on": "",
				"insert_after": "mohre_information"
			},
			{
				"fieldname": "labor_category_number",
				"fieldtype": "Data",
				"label": "Labor Category Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "no_of_employee_quota"
			},
			{
				"fieldname": "e_signature_card_obtained",
				"fieldtype": "Select",
				"label": "E-Signature Card Obtained",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Yes\nNo",
				"depends_on": "",
				"insert_after": "labor_category_number"
			},
			{
				"fieldname": "registered_mobile_number",
				"fieldtype": "Phone",
				"label": "Registered Mobile Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "e_signature_card_obtained"
			},
			{
				"fieldname": "registered_email_id",
				"fieldtype": "Data",
				"label": "Registered Email ID",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "registered_mobile_number"
			},
			{
				"fieldname": "registered_column",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "registered_email_id"
			},
			{
				"fieldname": "primary_contact_person",
				"fieldtype": "Phone",
				"label": "Primary Contact Person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "custom_column_break_bqi4w"
			},
			{
				"fieldname": "e_signature_card_holder_name",
				"fieldtype": "Data",
				"label": "E-Signature Card Holder Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_employees"
			},
			{
				"fieldname": "e_signature_card_holder_contact_no",
				"fieldtype": "Phone",
				"label": "E-Signature Card Holder Contact No",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "e_signature_card_holder_name"
			},
			{
				"fieldname": "e_signature_card_holder_email",
				"fieldtype": "Data",
				"label": "E-Signature Card Holder Email",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "e_signature_card_code_password"
			},
			{
				"fieldname": "e_signature_card_code_password",
				"fieldtype": "Data",
				"label": "E-Signature Card Code / Password",
				"reqd": 0,
				"in_list_view": 0,
				"options": "e_signature_card_code_password",
				"depends_on": "",
				"insert_after": "e_signature_card_holder_contact_no"
			},
			{
				"fieldname": "mohre_mobile_number",
				"fieldtype": "Phone",
				"label": "MOHRE Mobile Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "primary_contact_person"
			},
			{
				"fieldname": "mohre_landline_number",
				"fieldtype": "Data",
				"label": "MOHRE Landline Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "mohre_email_id"
			},
			{
				"fieldname": "mohre_email_id",
				"fieldtype": "Data",
				"label": "MOHRE Email ID",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "mohre_mobile_number"
			},
			{
				"fieldname": "total_employees",
				"fieldtype": "Int",
				"label": "Total Employees",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "registered_column"
			},
			{
				"fieldname": "visa_quota_increase_date",
				"fieldtype": "Date",
				"label": "Visa Quota Increase Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_female_visa_quota"
			},
			{
				"fieldname": "visa_column_break",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "visa_quota_increase_date"
			},
			{
				"fieldname": "total_visa_quota",
				"fieldtype": "Int",
				"label": "Total Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "custom_visa_detailes_"
			},
			{
				"fieldname": "used_visa_quota",
				"fieldtype": "Int",
				"label": "Used Visa Quota",
				"reqd": 0,
				"in_list_view": 1,
				"options": "",
				"depends_on": "",
				"insert_after": "quota_column_break"
			},
			{
				"fieldname": "quota_column_break",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 1,
				"options": "",
				"depends_on": "",
				"insert_after": "unused_female_visa_quota"
			},
			{
				"fieldname": "unused_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "visa_column_break"
			},
			{
				"fieldname": "total_male_visa_quota",
				"fieldtype": "Int",
				"label": "Total Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_visa_quota"
			},
			{
				"fieldname": "used_male_visa_quota",
				"fieldtype": "Int",
				"label": "Used Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "used_visa_quota"
			},
			{
				"fieldname": "unused_male_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "unused_visa_quota"
			},
			{
				"fieldname": "total_female_visa_quota",
				"fieldtype": "Int",
				"label": "Total Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_male_visa_quota"
			},
			{
				"fieldname": "used_female_visa_quota",
				"fieldtype": "Int",
				"label": "Used Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "used_male_visa_quota"
			},
			{
				"fieldname": "unused_female_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "unused_male_visa_quota"
			},
			{
				"fieldname": "dubai_chamber",
				"fieldtype": "Tab Break",
				"label": "Dubai Chamber",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "external_authority_permit_expiry_date"
			},
			{
				"fieldname": "custom_dubai_chamber_membership",
				"fieldtype": "Section Break",
				"label": "Dubai Chamber Membership",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "dubai_chamber"
			},
			{
				"fieldname": "custom_column_break_eobi8",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "establishment_card_expiry_date"
			},
			{
				"fieldname": "custom_column_break_aay8e",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "licensed_business_activity"
			},
			{
				"fieldname": "custom_column_break_bqi4w",
				"fieldtype": "Column Break",
				"label": "",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "e_signature_card_holder_email"
			},
			{
				"fieldname": "custom_visa_detailes_",
				"fieldtype": "Section Break",
				"label": "Visa Detailes",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "mohre_landline_number"
			},
			{
				"fieldname": "customer_name_in_arabic",
				"fieldtype": "Data",
				"label": "Customer Name in Arabic",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "customer_name"
			}
		],
		"Stakeholder Detail": [
			{
				"fieldname": "share_section_break",
				"fieldtype": "Section Break",
				"label": "Share Information",
				"depends_on": "eval:doc.is_shareholder == 1",
				"insert_after": "is_ubo"
			},
			{
				"fieldname": "share_type",
				"fieldtype": "Select",
				"label": "Share Type",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Individual\nCorporate",
				"depends_on": "",
				"insert_after": "share_section_break"
			},
			{
				"fieldname": "no_of_shares",
				"fieldtype": "Float",
				"label": "No of Shares",
				"reqd": 0,
				"in_list_view": 1,
				"options": "",
				"depends_on": "",
				"insert_after": "share_type"
			},
			{
				"fieldname": "share_capital",
				"fieldtype": "Currency",
				"label": "Share Capital",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "no_of_shares"
			},
			{
				"fieldname": "stake_in_shareholding",
				"fieldtype": "Percent",
				"label": "Stake in shareholding",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "share_capital"
			},
		]

	}