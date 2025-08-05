import frappe
from frappe.model.document import Document
from frappe.utils import nowdate, get_weekday

@frappe.whitelist(allow_guest=True)
def get_upcoming_availability(doctor):
    if not doctor:
        frappe.throw("Doctor is a required field", frappe.MandatoryError)

    days_map = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    today_index = get_weekday(nowdate())

    doc = frappe.get_doc("Doctor Availability", {"doctor": doctor})

    upcoming_days = []

   
    for child in doc.week:
        day_name = frappe.get_value("day of week", child.day_of_week, "name")

        day_index = days_map.get(day_name)
        if day_index is not None and day_index >= today_index:
            upcoming_days.append({
                "day_of_week": day_name,
                "start_time": doc.start_time,
                "end_time": doc.end_time
            })

    upcoming_days.sort(key=lambda d: days_map[d["day_of_week"]])

    return {
        "doctor": doctor,
        "upcoming_availability": upcoming_days
    }
