import time
import serial

if __name__ == "__main__":

    ser = serial.Serial(
        port="\\.\COM8",
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )

    ser.isOpen()

    print("Enter your commands below.\r\n"
          "Insert \"exit\" to leave the application.")

    while True:

        input_command = input(">> ")
        if input_command == "exit":
            ser.close()
            exit()
        else:

            bytes_input = bytes(input_command, "utf-8")
            ser.write(bytes_input)
            out = ""

            time.sleep(1)

            while ser.inWaiting() > 0:
                out += ser.read(1).decode("utf-8")
                # if ser.read(10).decode("utf-8") == r"\n":
                #     out += ser.read(1).decode("utf-8")
                # print(out)

            if out != "":
                print(">>", out)

