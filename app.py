import time
import pygame

def set_alarm():
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))
    tone = input("Enter the path to the tone file (e.g., sound.mp3): ")
    snooze_time = int(input("Enter snooze time in minutes: "))
    return hour, minute, tone, snooze_time

def play_alarm(tone):
    pygame.mixer.init()
    pygame.mixer.music.load(tone)
    pygame.mixer.music.play(-1)  # Play the alarm sound indefinitely

def stop_alarm():
    pygame.mixer.music.stop()

def snooze_alarm(snooze_time):
    print("Alarm snoozed for {} minutes.".format(snooze_time))
    time.sleep(snooze_time * 60)

def main():
    print("Alarm Clock")
    while True:
        hour, minute, tone, snooze_time = set_alarm()
        alarm_time = f"{hour:02d}:{minute:02d}"

        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                print("Wake up!")
                play_alarm(tone)
                response = input("Enter 'stop' to stop the alarm or 'snooze' to snooze it: ")
                if response.lower() == 'stop':
                    stop_alarm()
                    break
                elif response.lower() == 'snooze':
                    stop_alarm()
                    snooze_alarm(snooze_time)
                    break
            time.sleep(1)  # Check the current time every second

if __name__ == "__main__":
    main()
