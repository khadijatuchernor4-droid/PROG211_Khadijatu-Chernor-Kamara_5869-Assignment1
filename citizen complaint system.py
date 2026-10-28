"""
Citizen Complaint Management System
Course: PROG211 - Object-Oriented Programming 1
Domain: Government / Digital Public Goods

This is an educational demonstration. Do not enter real personal or sensitive data.
The program stores demonstration records in memory only; data is lost when it exits.
"""

from datetime import datetime


class Citizen:
    """Represents a citizen submitting a non-sensitive demonstration complaint."""

    def __init__(self, citizen_id, display_name):
        self.citizen_id = citizen_id
        self.display_name = display_name

    def display_info(self):
        """Return a short description of the citizen record."""
        return f"Citizen ID: {self.citizen_id} | Display name: {self.display_name}"


class Complaint:
    """Represents a complaint submitted to a public service office."""

    total_created = 0  # Class attribute shared by all Complaint objects

    def __init__(self, complaint_id, category, description, citizen):
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.citizen = citizen
        self.status = "Received"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        Complaint.total_created += 1

    def update_status(self, new_status):
        """Instance method: update the status of this complaint."""
        allowed_statuses = {"Received", "In Review", "Resolved", "Closed"}
        if new_status not in allowed_statuses:
            raise ValueError(
                "Status must be Received, In Review, Resolved, or Closed."
            )
        self.status = new_status

    def display_info(self):
        """Instance method: format this complaint for display."""
        return (
            f"{self.complaint_id} | {self.category} | {self.status}\n"
            f"  Description: {self.description}\n"
            f"  Submitted by: {self.citizen.display_name} "
            f"({self.citizen.citizen_id})\n"
            f"  Date: {self.created_at}"
        )

    @classmethod
    def get_total_created(cls):
        """Class method: report how many complaints were created in this run."""
        return cls.total_created

    @staticmethod
    def valid_category(category):
        """Static method: check whether a category is supported."""
        categories = {"Roads", "Water", "Sanitation", "Public Services", "Other"}
        return category in categories


class ComplaintSystem:
    """Manages complaint objects using a Python list."""

    def __init__(self):
        self.complaints = []  # Required data structure: a list
        self.next_number = 1

    def add_complaint(self, citizen_name, category, description):
        """Create and store a complaint, then return it."""
        if not citizen_name.strip():
            raise ValueError("Display name cannot be empty.")
        if not Complaint.valid_category(category):
            raise ValueError(
                "Choose Roads, Water, Sanitation, Public Services, or Other."
            )
        if not description.strip():
            raise ValueError("Description cannot be empty.")

        citizen = Citizen(f"C{self.next_number:03d}", citizen_name.strip())
        complaint = Complaint(
            f"CP{self.next_number:03d}", category, description.strip(), citizen
        )
        self.complaints.append(complaint)
        self.next_number += 1
        return complaint

    def display_all(self):
        """Display all stored complaints."""
        if not self.complaints:
            print("No complaints have been recorded.")
            return
        for complaint in self.complaints:
            print(complaint.display_info())
            print("-" * 55)

    def find_complaint(self, complaint_id):
        """Find one complaint by its reference number."""
        for complaint in self.complaints:
            if complaint.complaint_id.lower() == complaint_id.lower():
                return complaint
        return None


def run_demo():
    """Run a short sample that demonstrates the program's main features."""
    system = ComplaintSystem()

    print("=" * 55)
    print("CITIZEN COMPLAINT MANAGEMENT SYSTEM")
    print("Educational demo — use fictional names and non-sensitive details")
    print("=" * 55)

    first = system.add_complaint(
        "Demo Citizen A", "Roads", "A pothole needs attention near the market."
    )
    second = system.add_complaint(
        "Demo Citizen B", "Water", "The public tap is not working."
    )
    second.update_status("In Review")

    print("\nSAMPLE COMPLAINTS")
    system.display_all()
    print(f"Complaints created this run: {Complaint.get_total_created()}")

    found = system.find_complaint(first.complaint_id)
    if found:
        print(f"\nSearch result for {first.complaint_id}: {found.status}")


if __name__ == "__main__":
    run_demo()
