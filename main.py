
def estimate_cloud_cost():
    print("Cloud Cost Estimation Helper")
    print("----------------------------")

    try:
        hours = float(input("Enter usage hours: "))
        hourly_rate = float(input("Enter estimated hourly rate ($): "))

        if hours < 0 or hourly_rate < 0:
            print("Please enter values that are zero or greater.")
            return

        total_cost = hours * hourly_rate

        print("\nCost Estimation Result")
        print(f"Usage hours: {hours:g}")
        print(f"Hourly rate: ${hourly_rate:.2f}")
        print(f"Estimated total cost: ${total_cost:.2f}")
        print("\nNote: This is an estimate, not an actual cloud bill.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    estimate_cloud_cost()
