# Copyright (c) 2025, Ndungu Njuguna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class DoctorAvailability(Document):
    def validate(self):
        # Calculate today's day name dynamically
        today = datetime.now()
        day_name = today.strftime("%A") 

        # Convert days_available (MultiSelect) to list if needed
        if isinstance(self.days_available, str):
            available_days = [day.strip() for day in self.days_available.split(",")]
        else:
            available_days = self.days_available or []

        # Determine availability for today
        is_available_today = day_name in available_days

        # Update Doctor status
        if self.doctor:
            doc = frappe.get_doc("Doctor", self.doctor)
            new_status = "Available" if is_available_today else "Unavailable"
            
            # Update only if status changed for performance
            if doc.status != new_status:
                doc.status = new_status
                doc.save(ignore_permissions=True)  


