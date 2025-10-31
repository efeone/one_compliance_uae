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
				"insert_after": "license_registration_number"
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
				"insert_after": "moa_signing_date"
			},
			{
				"fieldname": "actual_business_activity",
				"fieldtype": "Small Text",
				"label": "Actual Business Activity",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "licensed_business_activity"
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
				"insert_after": "legal_column_break"
			},
			{
				"fieldname": "chamber_membership_start_date",
				"fieldtype": "Date",
				"label": "Chamber Membership Start Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "dubai_chamber_membership_number"
			},
			{
				"fieldname": "establishment_card_issue_date",
				"fieldtype": "Date",
				"label": "Establishment card issue date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "chamber_membership_start_date"
			},
			{
				"fieldname": "establishment_card_holder_name",
				"fieldtype": "Data",
				"label": "Establishment card holder name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "establishment_card_issue_date"
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
				"insert_after": "establishment_card_expiry_date"
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
				"insert_after": "registered_email_id_with_authority"
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
				"fieldname": "aml_record",
				"fieldtype": "Tab Break",
				"label": "AML Record",
				"options": "aml_record",
				"insert_after": "external_authority_permit_expiry_date"
			},
			{
				"fieldname": "aml_record_section",
				"fieldtype": "Tab Break",
				"label": "AML Record",
				"insert_after": "aml_record"
			},
			{
				"fieldname": "company_risk_category",
				"fieldtype": "Data",
				"label": "Company Risk Category",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "aml_record_section"
			},
			{
				"fieldname": "company_risk_status",
				"fieldtype": "Data",
				"label": "Company Risk Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "company_risk_category"
			},
			{
				"fieldname": "aml_column_break",
				"fieldtype": "Column Break",
				"insert_after": "company_risk_status"
			},
			{
				"fieldname": "shareholder_risk_status",
				"fieldtype": "Data",
				"label": "Shareholder Risk Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "aml_column_break"
			},
			{
				"fieldname": "shareholder_risk_category",
				"fieldtype": "Data",
				"label": "Shareholder Risk Category",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "shareholder_risk_status"
			},
			{
				"fieldname": "mohre_record",
				"fieldtype": "Tab Break",
				"label": "MOHRE Record",
				"reqd": 0,
				"in_list_view": 0,
				"options": "mohre_record",
				"depends_on": "",
				"insert_after": "shareholder_risk_category"
			},
			{
				"fieldname": "no_of_employee_quota",
				"fieldtype": "Data",
				"label": "No of Employee Quota (Ministry of Labor/Licensing Authority)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "no_of_employee_quota",
				"depends_on": "",
				"insert_after": "mohre_record"
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
				"fieldname": "primary_contact_person",
				"fieldtype": "Phone",
				"label": "Primary Contact Person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "registered_email_id"
			},
			{
				"fieldname": "e_signature_card_holder_name",
				"fieldtype": "Data",
				"label": "E-Signature Card Holder Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "primary_contact_person"
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
				"insert_after": "e_signature_card_holder_contact_no"
			},
			{
				"fieldname": "e_signature_card_code_password",
				"fieldtype": "Data",
				"label": "E-Signature Card Code / Password",
				"reqd": 0,
				"in_list_view": 0,
				"options": "e_signature_card_code_password",
				"depends_on": "",
				"insert_after": "e_signature_card_holder_email"
			},
			{
				"fieldname": "mohre_mobile_number",
				"fieldtype": "Phone",
				"label": "MOHRE Mobile Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "e_signature_card_code_password"
			},
			{
				"fieldname": "mohre_landline_number",
				"fieldtype": "Data",
				"label": "MOHRE Landline Number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "mohre_mobile_number"
			},
			{
				"fieldname": "mohre_column_break",
				"fieldtype": "Column Break",
				"insert_after": "mohre_landline_number"
			},
			{
				"fieldname": "mohre_email_id",
				"fieldtype": "Data",
				"label": "MOHRE Email ID",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "",
				"insert_after": "mohre_column_break"
			},
			{
				"fieldname": "total_employees",
				"fieldtype": "Int",
				"label": "Total Employees",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "mohre_email_id"
			},
			{
				"fieldname": "visa_quota_increase_date",
				"fieldtype": "Date",
				"label": "Visa Quota Increase Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_employees"
			},
			{
				"fieldname": "total_visa_quota",
				"fieldtype": "Int",
				"label": "Total Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "visa_quota_increase_date"
			},
			{
				"fieldname": "used_visa_quota",
				"fieldtype": "Int",
				"label": "Used Visa Quota",
				"reqd": 0,
				"in_list_view": 1,
				"options": "",
				"depends_on": "",
				"insert_after": "total_visa_quota"
			},
			{
				"fieldname": "unused_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "used_visa_quota"
			},
			{
				"fieldname": "total_male_visa_quota",
				"fieldtype": "Int",
				"label": "Total Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "unused_visa_quota"
			},
			{
				"fieldname": "used_male_visa_quota",
				"fieldtype": "Int",
				"label": "Used Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_male_visa_quota"
			},
			{
				"fieldname": "unused_male_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Male Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "used_male_visa_quota"
			},
			{
				"fieldname": "total_female_visa_quota",
				"fieldtype": "Int",
				"label": "Total Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "unused_male_visa_quota"
			},
			{
				"fieldname": "used_female_visa_quota",
				"fieldtype": "Int",
				"label": "Used Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "total_female_visa_quota"
			},
			{
				"fieldname": "unused_female_visa_quota",
				"fieldtype": "Int",
				"label": "Unused Female Visa Quota",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "used_female_visa_quota"
			},
			{
				"fieldname": "shareholding_and_management",
				"fieldtype": "Tab Break",
				"label": "Shareholding & Management",
				"reqd": 0,
				"in_list_view": 0,
				"options": "shareholding_and_management",
				"depends_on": "",
				"insert_after": "unused_female_visa_quota"
			},
			{
				"fieldname": "share_capital",
				"fieldtype": "Currency",
				"label": "Share Capital",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "shareholding_and_management"
			},
			{
				"fieldname": "no_of_shares",
				"fieldtype": "Int",
				"label": "No of Shares",
				"reqd": 0,
				"in_list_view": 1,
				"options": "",
				"depends_on": "",
				"insert_after": "share_capital"
			},
			{
				"fieldname": "shareholder_name",
				"fieldtype": "Data",
				"label": "Shareholder Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "no_of_shares"
			},
			{
				"fieldname": "shareholder_type",
				"fieldtype": "Data",
				"label": "Shareholder Type",
				"reqd": 0,
				"in_list_view": 0,
				"options": "shareholder_type",
				"depends_on": "",
				"insert_after": "shareholder_name"
			},
			{
				"fieldname": "stake_in_shareholding",
				"fieldtype": "Percent",
				"label": "Stake in shareholding",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "shareholder_type"
			},
			{
				"fieldname": "nationality_country_of_origin",
				"fieldtype": "Link",
				"label": "Nationality / Country of Origin",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Country",
				"depends_on": "",
				"insert_after": "stake_in_shareholding"
			},
			{
				"fieldname": "second_nationality",
				"fieldtype": "Data",
				"label": "Second Nationality",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "nationality_country_of_origin"
			},
			{
				"fieldname": "passport_expiry_date",
				"fieldtype": "Date",
				"label": "Passport Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "second_nationality"
			},
			{
				"fieldname": "is_individual_shareholder",
				"fieldtype": "Check",
				"label": "Is Individual Shareholder",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "passport_expiry_date"
			},
			{
				"fieldname": "other_designations_in_the_company",
				"fieldtype": "Link",
				"label": "Other Designations in the company",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Designation",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "is_individual_shareholder"
			},
			{
				"fieldname": "uae_contact_number",
				"fieldtype": "Phone",
				"label": "UAE Contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "other_designations_in_the_company"
			},
			{
				"fieldname": "uae_residential_address_individual_shareholder",
				"fieldtype": "Small Text",
				"label": "UAE/Residential Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uae_contact_number"
			},
			{
				"fieldname": "home_country_contact_number",
				"fieldtype": "Phone",
				"label": "Home Country contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uae_residential_address_individual_shareholder"
			},
			{
				"fieldname": "home_country_address",
				"fieldtype": "Small Text",
				"label": "Home Country Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "home_country_contact_number"
			},
			{
				"fieldname": "email_address_individual_shareholder",
				"fieldtype": "Data",
				"label": "Email Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Email",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "home_country_address"
			},
			{
				"fieldname": "uid_number",
				"fieldtype": "Data",
				"label": "UID number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "email_address_individual_shareholder"
			},
			{
				"fieldname": "uae_residency_status",
				"fieldtype": "Select",
				"label": "UAE Residency Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Resident\nNon-Resident",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uid_number"
			},
			{
				"fieldname": "uae_residency_visa_expiry_date",
				"fieldtype": "Date",
				"label": "UAE Residency Visa Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uae_residency_status"
			},
			{
				"fieldname": "uae_emirates_id_card_expiry_date",
				"fieldtype": "Date",
				"label": "UAE Emirates ID Card Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uae_residency_visa_expiry_date"
			},
			{
				"fieldname": "non_resident_uae_visit_history",
				"fieldtype": "Small Text",
				"label": "Non-Resident UAE Visit History",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "uae_emirates_id_card_expiry_date"
			},
			{
				"fieldname": "aml_status",
				"fieldtype": "Data",
				"label": "AML Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "non_resident_uae_visit_history"
			},
			{
				"fieldname": "poa_holder_exists",
				"fieldtype": "Select",
				"label": "POA Holder Exists",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Yes\nNo",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "aml_status"
			},
			{
				"fieldname": "domestic_or_foreign_pep",
				"fieldtype": "Data",
				"label": "Domestic or Foreign PEP",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "poa_holder_exists"
			},
			{
				"fieldname": "address_in_proof_of_address",
				"fieldtype": "Small Text",
				"label": "Address in Proof of Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_individual_shareholder",
				"insert_after": "domestic_or_foreign_pep"
			},
			{
				"fieldname": "is_corporate_shareholder",
				"fieldtype": "Check",
				"label": "Is Corporate Shareholder",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "address_in_proof_of_address"
			},
			{
				"fieldname": "corporate_shareholder_name",
				"fieldtype": "Data",
				"label": "Corporate Shareholder Name",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "is_corporate_shareholder"
			},
			{
				"fieldname": "country_of_incorporation",
				"fieldtype": "Link",
				"label": "Country of Incorporation",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Country",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "corporate_shareholder_name"
			},
			{
				"fieldname": "corporate_shareholder_address",
				"fieldtype": "Small Text",
				"label": "Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "country_of_incorporation"
			},
			{
				"fieldname": "corporate_shareholder_email_id",
				"fieldtype": "Data",
				"label": "Email ID",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "corporate_shareholder_address"
			},
			{
				"fieldname": "corporate_shareholder_tel_no",
				"fieldtype": "Data",
				"label": "Tel No",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "corporate_shareholder_email_id"
			},
			{
				"fieldname": "corporate_shareholder_registeration_no",
				"fieldtype": "Data",
				"label": "Registeration no",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_corporate_shareholder",
				"insert_after": "corporate_shareholder_tel_no"
			},
			{
				"fieldname": "non_shareholder_company_officers",
				"fieldtype": "Check",
				"label": "Non-Shareholder Company Representatives",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "corporate_shareholder_registeration_no"
			},
			{
				"fieldname": "individuals_person_name",
				"fieldtype": "Data",
				"label": "Name of the Person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "non_shareholder_company_officers"
			},
			{
				"fieldname": "company_designation",
				"fieldtype": "Link",
				"label": "Designations in the company",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Designation",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_person_name"
			},
			{
				"fieldname": "individuals_nationality",
				"fieldtype": "Data",
				"label": "Nationality",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "company_designation"
			},
			{
				"fieldname": "passport_expiry",
				"fieldtype": "Date",
				"label": "Passport Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_nationality"
			},
			{
				"fieldname": "individuals_contact_number",
				"fieldtype": "Phone",
				"label": "UAE contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "passport_expiry"
			},
			{
				"fieldname": "uae_resdiential_address",
				"fieldtype": "Small Text",
				"label": "UAE/Resdiential Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_contact_number"
			},
			{
				"fieldname": "individuals_home_country_number",
				"fieldtype": "Phone",
				"label": "Home country contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "uae_resdiential_address"
			},
			{
				"fieldname": "individuals_home_country_address",
				"fieldtype": "Small Text",
				"label": "Home Country Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_home_country_number"
			},
			{
				"fieldname": "individuals_email_address",
				"fieldtype": "Data",
				"label": "Email address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_home_country_address"
			},
			{
				"fieldname": "individuals_uid_number",
				"fieldtype": "Data",
				"label": "UID number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_email_address"
			},
			{
				"fieldname": "individuals__residency_status",
				"fieldtype": "Select",
				"label": "UAE residency Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Resident\nNon-Resident",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_uid_number"
			},
			{
				"fieldname": "individuals_residency_visa_expiry",
				"fieldtype": "Date",
				"label": "UAE Residency Visa Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals__residency_status"
			},
			{
				"fieldname": "individuals_emirates_id_expiry",
				"fieldtype": "Date",
				"label": "UAE Emirates ID Card Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_residency_visa_expiry"
			},
			{
				"fieldname": "individuals_aml_status",
				"fieldtype": "Data",
				"label": "AML Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_emirates_id_expiry"
			},
			{
				"fieldname": "individuals_domestic_or_foreign",
				"fieldtype": "Data",
				"label": "Domestic or Foreign PEP",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_aml_status"
			},
			{
				"fieldname": "address_in_proof",
				"fieldtype": "Small Text",
				"label": "Address in Proof of Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.non_shareholder_company_officers",
				"insert_after": "individuals_domestic_or_foreign"
			},
			{
				"fieldname": "shareholder_column_break",
				"fieldtype": "Column Break",
				"label": "Contact Person Details",
				"insert_after": "address_in_proof"
			},
			{
				"fieldname": "name_of_the_person",
				"fieldtype": "Data",
				"label": "Name of the Person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "shareholder_column_break"
			},
			{
				"fieldname": "designations_in_the_company",
				"fieldtype": "Link",
				"label": "Designations in the company",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Designation",
				"depends_on": "",
				"insert_after": "name_of_the_person"
			},
			{
				"fieldname": "individuals_passport_expiry_date",
				"fieldtype": "Date",
				"label": "Passport Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "designations_in_the_company"
			},
			{
				"fieldname": "contact_uae_number",
				"fieldtype": "Phone",
				"label": "UAE contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "individuals_passport_expiry_date"
			},
			{
				"fieldname": "home_country_contact",
				"fieldtype": "Phone",
				"label": "Home country contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "contact_uae_number"
			},
			{
				"fieldname": "uae_residency_visa_expiry",
				"fieldtype": "Date",
				"label": "UAE Residency Visa Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "home_country_contact"
			},
			{
				"fieldname": "uae_emirates_id_card_expiry",
				"fieldtype": "Date",
				"label": "UAE Emirates ID Card Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "uae_residency_visa_expiry"
			},
			{
				"fieldname": "contact_email_address",
				"fieldtype": "Data",
				"label": "Email address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "uae_emirates_id_card_expiry"
			},
			{
				"fieldname": "whatsapp_number",
				"fieldtype": "Data",
				"label": "Whatsapp number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "contact_email_address"
			},
			{
				"fieldname": "role_of_the_person",
				"fieldtype": "Data",
				"label": "Role of the person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "whatsapp_number"
			},
			{
				"fieldname": "is_ultimate_beneficial_owner",
				"fieldtype": "Check",
				"label": "Is Ultimate Beneficial Owner",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "",
				"insert_after": "role_of_the_person"
			},
			{
				"fieldname": "contact_person_name",
				"fieldtype": "Data",
				"label": "Name of the Person",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "is_ultimate_beneficial_owner"
			},
			{
				"fieldname": "nationality",
				"fieldtype": "Data",
				"label": "Nationality",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "contact_person_name"
			},
			{
				"fieldname": "ultimate_second_nationality",
				"fieldtype": "Data",
				"label": "Second Nationality",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "nationality"
			},
			{
				"fieldname": "contact_passport_expiry",
				"fieldtype": "Date",
				"label": "Passport Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_second_nationality"
			},
			{
				"fieldname": "ultimate_contact_number",
				"fieldtype": "Phone",
				"label": "UAE contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "contact_passport_expiry"
			},
			{
				"fieldname": "ultimate_residential_address",
				"fieldtype": "Small Text",
				"label": "UAE residential Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_contact_number"
			},
			{
				"fieldname": "home_contact_number",
				"fieldtype": "Phone",
				"label": "Home country contact number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_residential_address"
			},
			{
				"fieldname": "home_residential_address",
				"fieldtype": "Small Text",
				"label": "Home Country residential Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "home_contact_number"
			},
			{
				"fieldname": "email_address_corporate",
				"fieldtype": "Data",
				"label": "Email address (corporate)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "home_residential_address"
			},
			{
				"fieldname": "email_address_personal",
				"fieldtype": "Data",
				"label": "Email address (personal)",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "email_address_corporate"
			},
			{
				"fieldname": "ultimate_uid_number",
				"fieldtype": "Data",
				"label": "UID number",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "email_address_personal"
			},
			{
				"fieldname": "ultimate_residency_status",
				"fieldtype": "Select",
				"label": "UAE residency Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "Resident\nNon-Resident",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_uid_number"
			},
			{
				"fieldname": "ultimate_residency_visa_expiry",
				"fieldtype": "Date",
				"label": "UAE Residency Visa Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_residency_status"
			},
			{
				"fieldname": "ultimate_emirates_id_card_expiry_date",
				"fieldtype": "Date",
				"label": "UAE Emirates ID Card Expiry Date",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_residency_visa_expiry"
			},
			{
				"fieldname": "ultimate_aml_status",
				"fieldtype": "Data",
				"label": "AML Status",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_emirates_id_card_expiry_date"
			},
			{
				"fieldname": "ultimate_other_details",
				"fieldtype": "Small Text",
				"label": "Other Details",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_aml_status"
			},
			{
				"fieldname": "ultimate_domestic_foreign",
				"fieldtype": "Data",
				"label": "Domestic or Foreign PEP",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_other_details"
			},
			{
				"fieldname": "ultimate_address_in_address",
				"fieldtype": "Small Text",
				"label": "Address in Proof of Address",
				"reqd": 0,
				"in_list_view": 0,
				"options": "",
				"depends_on": "eval:doc.is_ultimate_beneficial_owner",
				"insert_after": "ultimate_domestic_foreign"
			}
		]
	}