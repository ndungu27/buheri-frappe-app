from frappe.model.document import Document
import frappe

class DoctorAvailability(Document):

    def on_update(self):
        doctor_doc = frappe.get_doc('Doctor', self.doctor)
        doctor_doc.update_status_based_on_availability()
