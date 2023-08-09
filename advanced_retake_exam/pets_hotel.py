def accommodate_new_pets(available_capacity, max_weight_limit, *pets):
    accommodated_pets = {}

    for pet_type, pet_weight in pets:
        if available_capacity > 0:
            if pet_weight <= max_weight_limit:
                available_capacity -= 1
                if pet_type in accommodated_pets:
                    accommodated_pets[pet_type] += 1
                elif pet_type not in accommodated_pets:
                    accommodated_pets[pet_type] = 1

    if available_capacity <= 0:
        result = "You did not manage to accommodate all pets!"
    else:
        result = f"All pets are accommodated! Available capacity: {available_capacity}."

    accommodated_pets = sorted(accommodated_pets.items())

    output = [result, "Accommodated pets:"]
    for pet_type, number in accommodated_pets:
        output.append(f"{pet_type}: {number}")

    return "\n".join(output)

