import sys

inn = sys.stdin
jon_say = next(inn).strip()
doctor_hear = next(inn).strip()
if len(jon_say) <= len(doctor_hear):
    print("no")
else:
    print("go")