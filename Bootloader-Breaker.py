import os
import sys

def main():
    code = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000000000000
    while True:
        command = f"clear && fastboot oem unlock {code}"
        print(f"Trying: {command}")
        if os.system(command) == 0:
            print(f"\n✅ CODE FOUND: {code}")
            break
        code += 1

if __name__ == "__main__":
    main()

