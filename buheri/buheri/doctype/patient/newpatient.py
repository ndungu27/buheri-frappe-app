import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)  
def register_patient():
    data = frappe.local.form_dict

    patient_name = data.get('patient_name')
    last_name = data.get('last_name')
    dob = data.get('dob')  # yyyy-mm-dd
    gender = data.get('gender')
    phone_number = data.get('phone_number')
    identification = data.get('identification')
    id_number =data.get('id_number')
    registration_date =data.get('registration_date')
    patient_status = data.get('patient_status')

    # Basic validation
    if not patient_name or not last_name or not gender or not dob:
        frappe.throw(_("Missing required fields. Please provide patient_name, last_name, gender, and dob."))

    # Create Patient document
    patient = frappe.get_doc({
        "doctype": "Patient",
        "patient_name": patient_name,
        "last_name": last_name,
        "gender": gender,
        "dob": dob,
        "phone_number": phone_number,
        "identification": identification,
        "id_number": id_number,
        "registration_date":registration_date,
        "patient_status":patient_status

    })

    patient.insert()
    frappe.db.commit()

    # Return the auto-generated patient ID (name)
    return {
        "message": "Patient registered successfully",
        "patient_id": patient.name
    }
