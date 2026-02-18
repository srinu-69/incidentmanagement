from create_incident import create_incident
from read_incidents import list_incidents, get_incident_by_id
from update_incident import update_status, update_description, update_severity
from delete_incident import delete_incident


def print_incident(it):
	print(f"ID: {it.get('id')}")
	print(f"Service: {it.get('service')}")
	print(f"Severity: {it.get('severity')}")
	print(f"Status: {it.get('status')}")
	print(f"Description: {it.get('description')}")
	print(f"Created: {it.get('created_at')}")
	print('-' * 40)


def menu():
	while True:
		print("Incident Management Tracker")
		print("1) Create incident")
		print("2) View all incidents")
		print("3) Update incident")
		print("4) Delete incident (resolved only)")
		print("5) Exit")
		choice = input("Choose: ").strip()

		if choice == '1':
			service = input("Service name: ").strip()
			severity = input("Severity (SEV1/SEV2/SEV3): ").strip()
			desc = input("Description: ").strip()
			inc = create_incident(service, severity, desc)
			print("Created:")
			print_incident(inc)

		elif choice == '2':
			items = list_incidents()
			if not items:
				print("No incidents")
			for it in items:
				print_incident(it)

		elif choice == '3':
			iid = input("Incident ID: ").strip()
			if not get_incident_by_id(iid):
				print("Not found")
			else:
				print("Update (1) Status  (2) Description  (3) Severity")
				opt = input("Choose: ").strip()
				if opt == '1':
					ns = input("New status (Open/Investigating/Mitigated/Resolved): ").strip()
					ok, msg = update_status(iid, ns)
					print(msg)
				elif opt == '2':
					nd = input("New description: ").strip()
					if update_description(iid, nd):
						print("Updated description")
					else:
						print("Failed to update")
				elif opt == '3':
					ns = input("New severity (SEV1/SEV2/SEV3): ").strip()
					if update_severity(iid, ns):
						print("Updated severity")
					else:
						print("Failed to update severity")
				else:
					print("Invalid option")

		elif choice == '4':
			iid = input("Incident ID to delete: ").strip()
			ok, msg = delete_incident(iid)
			print(msg)

		elif choice == '5':
			print("Goodbye")
			break
		else:
			print("Invalid choice")


if __name__ == '__main__':
	menu()

