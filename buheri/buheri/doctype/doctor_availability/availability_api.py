import frappe
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

    today_str = get_weekday(nowdate()) 
    today_index = days_map.get(today_str)
    if today_index is None:
        frappe.throw(f"Invalid weekday name '{today_str}' returned from get_weekday")

    availability_names = frappe.get_all(
        "Doctor Availability",
        filters={"doctor": doctor},
        pluck="name"
    )

    if not availability_names:
        return {"doctor": doctor, "upcoming_availability": []}

    doc = frappe.get_doc("Doctor Availability", availability_names[0])

    days_available = getattr(doc, "days_available", [])
    if not days_available:
        return {"doctor": doctor, "upcoming_availability": []}

    upcoming_days = []

    for child in days_available:
        day_name = frappe.get_value("day of week", child.day_of_week, "name")
        if not day_name:
            continue
        day_name = day_name.capitalize()
        day_index = days_map.get(day_name)
        if day_index is None:
            continue

        if day_index >= today_index:
            upcoming_days.append({
                "day_of_week": day_name,
                "start_time": getattr(child, 'start_time', doc.start_time),
                "end_time": getattr(child, 'end_time', doc.end_time)
            })

    upcoming_days.sort(key=lambda d: days_map[d["day_of_week"]])

    return {
        "doctor": doctor,
        "upcoming_availability": upcoming_days
    }

