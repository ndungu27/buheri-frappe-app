# Copyright (c) 2025, Ndungu Njuguna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Appointment(Document):
	def validate(self):
		if self.doctor and self.appointment_date:

			leave_exists = frappe.db.exists({
				"doctype":"Doctor Leave",
				"doctor" :self.doctor,
				"leave_start_date":["<=", self.appointment_date],
				"leave_end_date": [">=", self.appointment_date],
                "docstatus": 1  
            })
			if leave_exists:
				frappe.throw(f"Doctor {self.doctor} is on leave on {self.appointment_date}. Cannot book appointment.")
			


