import subprocess

# Replace 'your_script.py' with the name of the Python file you want to run
script_name = r"D:\ASEB\Semester 3\Projects\AI\ai project start part\verify.py"
print("\t\t\t\t\t\t\tWELCOME TO 50 SHADES OF FLAVOR")
print("Please hold up your ID card for the verification process.. ")
# Run the script
while True:
    ans=input("enter 's' or 'start' to start:   ").lower()
    if(ans=='s' or ans=='start'):
        break
    elif(not ans):
        continue
    else:
        print("not correct")
        continue
subprocess.call(['python', script_name])