import frappe

@frappe.whitelist(allow_guest=True)
def get_appointments_by_id(name=None):
    if name:
        appointment=frappe.get_doc("Appointment", name)

        if not appointment:
            frappe.throw("Appointment not found")

        return{
            "status":"200",
            "appointment":appointment.as_dict()
        }
    
    else:
        appointments=frappe.get_all("Appointment",
                                    fields=["name","patient","doctor","appointment_date","time","appointment_status"],
                                    order_by="appointment_date desc, time desc")
        return{
            "status":"200",
            "appointments":appointments,
            "count":len(appointments)
        }

    
