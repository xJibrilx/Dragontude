# =========================================
# U2 Dragon Man
# Treadmill Altitude Conversion System
# =========================================

# Formula:
# Altitude = 120 * (mph^2) * incline


def equivalent_altitude(mph, incline):
    return 120 * (mph ** 2) * incline


def main():

    print("=" * 55)
    print("               U2 DRAGON MAN")
    print("     TREADMILL ALTITUDE CONVERSION SYSTEM")
    print("=" * 55)

    while True:

        # MPH INPUT
        try:
            mph = float(input("\nEnter Speed MPH (0 - 12): "))

            if mph < 0 or mph > 12:
                print("ERROR: MPH must be between 0 and 12.")
                continue

        except ValueError:
            print("ERROR: Invalid MPH input.")
            continue

        # INCLINE INPUT
        try:
            incline = float(input("Enter Incline Level (0 - 15): "))

            if incline < 0 or incline > 15:
                print("ERROR: Incline must be between 0 and 15.")
                continue

        except ValueError:
            print("ERROR: Invalid incline input.")
            continue

        # CALCULATE ALTITUDE
        altitude = equivalent_altitude(mph, incline)

        # RESULTS
        print("\n" + "=" * 55)
        print("                 FLIGHT DATA")
        print("=" * 55)
        print(f"Speed          : {mph:.1f} mph")
        print(f"Incline        : {incline:.1f}")
        print(f"Dragon Altitude: {altitude:,.0f} ft")
        print("=" * 55)

        # CONTINUE
        again = input("\nRun another flight calculation? (y/n): ").lower()

        if again != "y":
            print("\nU2 Dragon Man shutting down...")
            break


if __name__ == "__main__":
    main()
