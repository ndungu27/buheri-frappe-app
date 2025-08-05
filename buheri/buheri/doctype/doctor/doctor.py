# Copyright (c) 2025, Ndungu Njuguna and contributors
# For license information, please see license.txt

from buheri.buheri.doctype import doctor_availability
from buheri.buheri.doctype.doctor_availability.doctor_availability import DoctorAvailability
import frappe
from frappe.model.document import Document
#from frappe.utils import validate_type
 


class Doctor(Document):
    


	# is_valid = validate_type(email, "email")
	# if is_valid:
	# 	"Email is valid"
	# else:
	# 	"Email is invalid"
		
	def doctor_available(self):
		self.availble = DoctorAvailability.doc_available
		return self.availble
	
	def doctor_unavailable(self):
		self.unavailable = DoctorAvailability.doc_unavailable
		return self.unavailable
		
	def before_save(self):
		self.full_name = f'{self.first_name}{self.last_name or ""}'
		Doctor.doctor_available
		Doctor.doctor_unavailable
	

	
