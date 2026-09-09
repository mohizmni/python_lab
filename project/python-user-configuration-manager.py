def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:"

    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}"

    return result + "\n"


test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

# Example usage
print(add_setting(test_settings, ("VOLUME", "HIGH")))
print(update_setting(test_settings, ("THEME", "DARK")))
print(delete_setting(test_settings, "LANGUAGE"))
print(view_settings(test_settings))