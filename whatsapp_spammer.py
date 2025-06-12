import pyautogui
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def show_banner():
    print(Fore.GREEN + Style.BRIGHT + "\n===========================================")
    print(Fore.CYAN + Style.BRIGHT + "        WhatsApp Message Spammer Tool")
    print(Fore.GREEN + Style.BRIGHT + "===========================================\n")
    
    print(Fore.RED + Style.BRIGHT + "⚠️ WARNING: This tool is for educational purposes only.")
    print(Fore.RED + Style.BRIGHT + "❌ Do not use this tool for spamming or harassment.")
    print(Fore.RED + Style.BRIGHT + "✔️ Use responsibly in ethical hacking or testing scenarios only.\n")
    
    print(Fore.MAGENTA + Style.BRIGHT + "🔹 Author  : Sherkhan")
    print(Fore.MAGENTA + Style.BRIGHT + "🔗 LinkedIn: https://www.linkedin.com/in/sherkhan-sk/\n")

def whatsapp_spammer():
    show_banner()

    print(Fore.YELLOW + "💬 Enter 3 different messages to rotate:")
    msg1 = input(Fore.YELLOW + "  ➊ Message 1: ")
    msg2 = input(Fore.YELLOW + "  ➋ Message 2: ")
    msg3 = input(Fore.YELLOW + "  ➌ Message 3: ")
    messages = [msg1, msg2, msg3]

    while True:
        try:
            count = int(input(Fore.YELLOW + "🔢 Enter how many times to send (1 - 999999): "))
            if 1 <= count <= 999999:
                break
            else:
                print(Fore.RED + "❌ Please enter between 1 and 999999.")
        except ValueError:
            print(Fore.RED + "❌ Invalid number.")

    while True:
        try:
            delay = float(input(Fore.YELLOW + "⏱️  Enter delay between rounds (0.1 - 10 seconds): "))
            if 0.1 <= delay <= 10:
                break
            else:
                print(Fore.RED + "❌ Delay must be between 0.1 and 10 seconds.")
        except ValueError:
            print(Fore.RED + "❌ Invalid number.")

    print(Fore.BLUE + "\n⏳ You have 5 seconds to open WhatsApp chat window...")
    time.sleep(5)

    print(Fore.GREEN + "🚀 Starting message spam...\n")

    for i in range(count):
        for j in range(3):  # Send 3 different messages in each round
            pyautogui.typewrite(messages[j % 3])
            pyautogui.press("enter")
        print(Fore.CYAN + f"✅ Sent batch {i+1}/{count}")
        time.sleep(delay)

    print(Fore.GREEN + "\n🎉 Done! All messages sent successfully.")

if __name__ == "__main__":
    whatsapp_spammer()

