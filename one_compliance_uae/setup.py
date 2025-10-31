import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

from one_compliance_uae.custom.custom_field.customer import get_customer_custom_fields

def after_install():
	#Creating PW IOI specific custom fields
	create_custom_fields(get_custom_fields(), ignore_validate=True)

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
	return custom_fields

