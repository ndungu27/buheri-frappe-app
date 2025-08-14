import frappe
from datetime import datetime

def update_doctors_status_daily():
    today = datetime.now().strftime("%A")
    
    doctors = frappe.get_all("Doctor", fields=["name"])

    for doctor in doctors:
        availability_records = frappe.get_all('DoctorAvailability', filters={'doctor': doctor.name})

        is_available = False
        for record in availability_records:
            doc = frappe.get_doc('DoctorAvailability', record.name)
            days = doc.days_available
            if isinstance(days, str):
                days_list = [d.strip() for d in days.split(",")]
            else:
                days_list = days or []

            if today in days_list:
                is_available = True
                break
        
        new_status = "Available" if is_available else "Unavailable"

        doctor_doc = frappe.get_doc("Doctor", doctor.name)
        if doctor_doc.status != new_status:
            doctor_doc.status = new_status
            doctor_doc.save(ignore_permissions=True)
