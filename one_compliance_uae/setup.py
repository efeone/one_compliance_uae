import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

from one_compliance_uae.custom.custom_field.customer import get_customer_custom_fields
from one_compliance_uae.custom.custom_field.opportunity import get_opportunity_custom_fields
from one_compliance_uae.custom.custom_field.opportunity_item import get_opportunity_item_custom_fields
from one_compliance_uae.custom.custom_field.multi_company_detail import get_multi_company_detail_custom_fields

def after_install():
	#Creating PW IOI specific custom fields
	create_custom_fields(get_custom_fields(), ignore_validate=True)
	create_property_setters(get_property_setters())

def after_migrate():
	after_install()

def before_uninstall():
	delete_custom_fields(get_custom_fields())

def delete_custom_fields(custom_fields: dict):
	'''
		Method to Delete custom fields
		args:
			custom_fields: a dict like `{'Task': [{fieldname: 'your_fieldname', ...}]}`
	'''
	for doctype, fields in custom_fields.items():
		frappe.db.delete(
			"Custom Field",
			{
				"fieldname": ("in", [field["fieldname"] for field in fields]),
				"dt": doctype,
			},
		)
		frappe.clear_cache(doctype=doctype)

def get_custom_fields():
	'''
		Method to get all custom fields that need to be created for PW IT Helpdesk and CM
	'''
	custom_fields = get_customer_custom_fields()
	custom_fields.update(get_opportunity_custom_fields())
	custom_fields.update(get_opportunity_item_custom_fields())
	custom_fields.update(get_multi_company_detail_custom_fields())
	return custom_fields

def create_property_setters(property_setter_datas):
	'''
	Method to create custom property setters
	args:
		property_setter_datas : list of dict of property setter obj
	'''
	for property_setter_data in property_setter_datas:
		if frappe.db.exists("Property Setter", property_setter_data):
			continue
		property_setter = frappe.new_doc("Property Setter")
		property_setter.update(property_setter_data)
		property_setter.flags.ignore_permissions = True
		property_setter.insert()

def get_property_setters():
	'''
	 specific property setters that need to be added to the DocTypes
	'''
	return [
		{
			"doctype_or_field": "DocField",
			"doc_type": "Customer",
			"field_name": "custom_customer_company_details",
			"property": "label",
			"property_type": "Data",
			"value": "Company Details"
		}
	]