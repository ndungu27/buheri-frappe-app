from frappe.model.document import Document
import frappe
from frappe.utils import today
import datetime


class Doctor(Document):

    def update_status_based_on_availability(self):
        today_day = datetime.datetime.strptime(today(), "%Y-%m-%d").strftime("%A")

        availability_records = frappe.get_all('Doctor Availability', filters={'doctor': self.name}, fields=['name'])

        available_today = False
        for record in availability_records:
            days = frappe.get_all('week', filters={'parent': record.name}, fields=['day_of_week'])
            day_names = [d.day_of_week for d in days]

            if today_day in day_names:
                available_today = True
                break

        status = "Available" if available_today else "Unavailable"
        if self.status != status:
            self.status = status
            self.save()
