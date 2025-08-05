# Copyright (c) 2025, Ndungu Njuguna and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document



class DoctorLeave(Document):
	def validate(self):
		if self.leave_end_date <= self.leave_start_date:
			frappe.throw("End Date must be after start date")
