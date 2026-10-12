# Assignment 4 – Inventory File System
# Build a program that reads employee attendance data from a text/CSV file (each line containing employee name, date and status: Present/Absent) and analyzes attendance patterns, producing a full report.
# Requirements:
# •	Read attendance records from a file attendance.csv using the csv module or manual line parsing.
# •	Calculate the total number of present and absent days for each employee.
# •	Identify and report any employee whose attendance percentage is below 75%.
# •	Write a summary report back out to a new file (attendance_report.txt) using the with statement in write mode.
# •	Provide a way to append a new day's attendance data to the source file without overwriting existing records.
# •	Handle missing files or malformed lines gracefully using appropriate checks.


# import csv
# import json
# with open("attendance2.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["NAME","Date","Status"])
#     writer.writerow(["Arun","23-10-2026","present"])
#     writer.writerow(["Arun","24-10-2026","present"])
#     writer.writerow(["Arun","25-10-2026","absent"])
#     writer.writerow(["Meera","23-10-2026","present"])
#     writer.writerow(["Meera","24-10-2026","absent"])
#     writer.writerow(["Meera","25-10-2026","absent"])
#     writer.writerow(["Akhil","23-10-2026","present"])
#     writer.writerow(["Akhil","24-10-2026","present"])
#     writer.writerow(["Akhil","25-10-2026","present"])
#     writer.writerow(["kiran","23-10-2026","absent"])
#     writer.writerow(["kiran","24-10-2026","absent"])
#     writer.writerow(["kiran","25-10-2026","absent"])
# print("attendance csv file created sucess")
# employees = {}
# with open("attendance2.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)  
#     for row in reader:
#         if len(row) == 3:
#             name = row[0]
#             status = row[2].lower()
#             if status == "present" or status == "absent":
#                 if name not in employees:
#                     employees[name] = {"present": 0, "absent": 0}
#                 employees[name][status] += 1
# with open("attendance_report.txt", "w") as file:
#     file.write("EMPLOYEE ATTENDANCE REPORT\n\n")
#     for name, data in employees.items():
#         present = data["present"]
#         absent = data["absent"]
#         total = present + absent
#         percentage = (present / total) * 100
#         file.write(f"Name: {name}\n")
#         file.write(f"Present Days: {present}\n")
#         file.write(f"Absent Days: {absent}\n")
#         file.write(f"Attendance Percentage: {percentage:.2f}%\n")
#         if percentage < 75:
#             file.write("Warning: Attendance below 75%\n")
#         file.write("-------------------------\n")
# print("Attendance report generated successfully!")
