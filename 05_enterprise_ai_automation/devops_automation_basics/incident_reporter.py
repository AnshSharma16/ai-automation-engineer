from datetime import datetime

LOG_FILE = "system.log"
REPORT_FILE = "incident_report.txt"

def generate_report():

    with open(LOG_FILE, "r") as log:
        lines = log.readlines()

    incidents = []

    for line in lines:

        if "ERROR" in line or "WARNING" in line:
            incidents.append(line)

    if incidents:

        with open(REPORT_FILE, "w") as report:

            report.write("Incident Report\n")
            report.write("Generated at: " + str(datetime.now()) + "\n\n")

            for incident in incidents:
                report.write(incident)

        print("Incident report generated")

    else:

        print("No incidents found")

generate_report()