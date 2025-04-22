import pandas as pd
import time
from datetime import datetime

# Simulated RFID Readings (For real systems, integrate with an actual RFID reader API)
class RFIDReader:
    def __init__(self):
        self.teddy_bear_ids = ['TB001', 'TB002', 'TB003', 'TB004']
    
    def read_rfid(self):
        # Simulate reading RFID tags from the warehouse entry/exit
        return self.teddy_bear_ids[time.localtime().tm_sec % len(self.teddy_bear_ids)]

# Simulate tracking attendance
def track_attendance():
    reader = RFIDReader()
    attendance_data = []
    
    while True:
        # Get the current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Simulate reading RFID tag
        teddy_id = reader.read_rfid()
        
        # Record attendance data
        attendance_data.append({
            'Teddy_ID': teddy_id,
            'Entry_Time': current_time
        })
        
        print(f"Attendance Recorded: {teddy_id} at {current_time}")
        
        # Save attendance every 10 seconds (simulated)
        if len(attendance_data) >= 5:
            df = pd.DataFrame(attendance_data)
            df.to_csv('teddy_attendance.csv', index=False)
            print("Attendance data saved to teddy_attendance.csv")
            attendance_data = []
        
        time.sleep(10)

if __name__ == '__main__':
    track_attendance()
