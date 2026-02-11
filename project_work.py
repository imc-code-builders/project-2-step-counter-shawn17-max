from data.utils import read_csv
STEP_THRESHOLD = 120

def get_changes(magnitudes):
    """Calculate changes between consecutive values.

    magnitudes = [100, 200, 50, 100]
    changes = [200 - 100, 50 - 200, 100 - 50] = [100, "-150," 50]

    Args:
        magnitudes: A list of acceleration readings in chronological order.

    Returns:
        A list containing the change in acceleration between each pair of
        consecutive readings.

    NOTE: Your return list should always be one element smaller than the input
    list. Why is that?

    EXAMPLE: if magnitudes = [100, 200, 50, 100], this function should return
    [100, "-150," 50]
    """
    changes = []
    # Iterate through the list up to the second-to-last element
    for i in range(len(magnitudes) - 1):
        # Calculate the change between the current and the next value
        change = magnitudes[i+1] - magnitudes[i]
        changes.append(change)
    return changes

def count_peaks(changes, threshold):
    """Count how many changes are above threshold.

    count = 0
    for change in changes:
        if change >= threshold:
            count += 1

    Args:
        changes: A list of changes in acceleration in chronological order.
        threshold: A number above which we consider an acceleration change to
        indicate a step.

    Returns:
        The number of acceleration changes greater than the threshold.

    EXAMPLE: if changes = [800, 100, 900, 400] and threshold = 700, this
    function should return 2.
    """
    step_count = 0
    # Iterate through the changes list and increment count if the change is above the threshold
    for change in changes:
        if change >= threshold:
            step_count += 1
    return step_count

def count_steps(magnitudes, threshold=STEP_THRESHOLD):
    """Main function: use other functions to count steps.

    Args:
        magnitudes: A list of acceleration readings in chronological order.
        threshold: the minimum acceleration change that is considered a step.

    Returns:
        The number of steps the user took.
    """
    # Use get_changes() to calculate differences between consecutive readings
    changes = get_changes(magnitudes)
    # Use count_peaks() to count how many of those changes are above the threshold
    number_of_steps = count_peaks(changes, threshold)
    return number_of_steps

if __name__ == "__main__":
    try:
        # NOTE: This assumes data.utils exists and the CSV file is present.
        times, magnitudes = read_csv("data/sample_data.csv")
        step_count = count_steps(magnitudes)
        print(f"Loaded {len(magnitudes)} data points")
        print(f"Detected {step_count} steps")
    except Exception as e:
        print(f"Error: {e}")
        print("Run tests.py to see what needs to be fixed.")
