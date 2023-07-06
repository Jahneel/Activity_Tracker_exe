from calender_service import create_event
from utils import get _user_input 

def main():

    summary = input("Enter activity name:")
    location = input("Enter location:")  
    start_time = input("Enter start time(YYYY-MM-DD HH:MM):")
    end_time= input("Enter end time(YYYY-MM-DD HH:MM):")

    create_event(summary, location, start_time, end_time)

if __name__ == "__main__":
    main()
