import carla

def load_custom_map(xodr_path):
    client = carla.Client('localhost', 2000)
    client.set_timeout(30.0)  # Increased timeout to 30 seconds

    # Load the OpenDRIVE file into CARLA
    with open(xodr_path, 'r') as file:
        xodr_data = file.read()

    # Generate the world from the xodr data
    try:
        world = client.generate_opendrive_world(xodr_data)
        print("Map loaded successfully!")
    except RuntimeError as e:
        print(f"Failed to load map: {e}")

if __name__ == "__main__":
    xodr_path = 'D:/CARLA_0.9.11/WindowsNoEditor/PythonAPI/util/opendrive/lucknow_fixed.xodr'
    load_custom_map(xodr_path)
