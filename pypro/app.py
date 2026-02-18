from create_incident import create_incident
from read_incidents import list_incidents, get_incident_by_id
from update_incident import update_status, update_description, update_severity
from delete_incident import delete_incident
from flask import Flask, request, jsonify, render_template, url_for, redirect


def print_incident(it):
	print(f"ID: {it.get('id')}")
	print(f"Service: {it.get('service')}")
	print(f"Severity: {it.get('severity')}")
	print(f"Status: {it.get('status')}")
	print(f"Description: {it.get('description')}")
	print(f"Created: {it.get('created_at')}")
	print('-' * 40)

app = Flask("webApp1")

@app.route("/", methods=['GET', 'POST'])
def Index():
    if request.method == "POST":
        operation = request.form.get("operation")
        if operation == "create":
            return redirect(url_for("create"))
        elif operation in ["update", "delete"]:
            return redirect(url_for("search"))
        return "Invalid operation", 400
    # Render a homepage or form for GET requests
    return render_template("index.html")
		

@app.route("/create", methods=['GET','POST'])
def create():
	service = request.form.get("service")
	severity = request.form.get("severity")
	desc = request.form.get("description")
	inc = create_incident(service, severity, desc)
	return render_template("create_incident.html", incident=inc, operation="created")


@app.route("/search", methods=['GET','POST'])
def search():
    incidents = list_incidents()
    return render_template('search_incident.html', incidents=incidents)


@app.route('/update/<iid>', methods=['GET', 'POST'])
def update(iid):
    # Make sure ID is string (since your JSON likely stores string IDs)
    iid = str(iid)
    incident = get_incident_by_id(iid)
    if not incident:
        return "Incident not found"
    if request.method == 'POST':
        field = request.form.get('field')
        value = request.form.get('value')
        if field == 'status':
            update_status(iid, value)
        elif field == 'description':
            update_description(iid, value)
        elif field == 'severity':
            update_severity(iid, value)
        return redirect(url_for('index'))
    return render_template('update_incident.html', incident=incident)

@app.route('/delete/<iid>', methods=['GET', 'POST'])
def delete(iid):
    iid = str(iid)
    incident = get_incident_by_id(iid)
    if not incident:
        return "Incident not found"
    if request.method == 'POST':
        ok, msg = delete_incident(iid)
        if not ok:
            return f"Delete Failed: {msg}"
        return redirect(url_for('index'))
    return render_template('delete_incident.html', incident=incident)
		
@app.route("/result", methods=['GET'])
def result():
    incident = request.args.get("incident")
    operation = request.args.get("operation")
    return render_template("result.html", incident=incident, operation=operation)


	# while True:
	# 	# print("Incident Management Tracker")
	# 	# print("1) Create incident")
	# 	# print("2) View all incidents")
	# 	# print("3) Update incident")
	# 	# print("4) Delete incident (resolved only)")
	# 	# print("5) Exit")
	# 	choice = input("Choose: ").strip()

	# 	if choice == '1':
	# 		service = input("Service name: ").strip()
	# 		severity = input("Severity (SEV1/SEV2/SEV3): ").strip()
	# 		desc = input("Description: ").strip()
	# 		inc = create_incident(service, severity, desc)
	# 		print("Created:")
	# 		print_incident(inc)

	# 	elif choice == '2':
	# 		items = list_incidents()
	# 		if not items:
	# 			print("No incidents")
	# 		for it in items:
	# 			print_incident(it)

	# 	elif choice == '3':
	# 		iid = input("Incident ID: ").strip()
	# 		if not get_incident_by_id(iid):
	# 			print("Not found")
	# 		else:
	# 			print("Update (1) Status  (2) Description  (3) Severity")
	# 			opt = input("Choose: ").strip()
	# 			if opt == '1':
	# 				ns = input("New status (Open/Investigating/Mitigated/Resolved): ").strip()
	# 				ok, msg = update_status(iid, ns)
	# 				print(msg)
	# 			elif opt == '2':
	# 				nd = input("New description: ").strip()
	# 				if update_description(iid, nd):
	# 					print("Updated description")
	# 				else:
	# 					print("Failed to update")
	# 			elif opt == '3':
	# 				ns = input("New severity (SEV1/SEV2/SEV3): ").strip()
	# 				if update_severity(iid, ns):
	# 					print("Updated severity")
	# 				else:
	# 					print("Failed to update severity")
	# 			else:
	# 				print("Invalid option") 

	# 	elif choice == '4':
	# 		iid = input("Incident ID to delete: ").strip()
	# 		ok, msg = delete_incident(iid)
	# 		print(msg)

	# 	elif choice == '5':
	# 		print("Goodbye")
	# 		break

	# 	else:
	# 		print("Invalid choice")
	





# if __name__ == '__main__':
# 	menu()
if __name__ == '__main__':
    app.run(debug=True)
