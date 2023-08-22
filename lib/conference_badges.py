def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    assignments = []
    for index, speaker in enumerate(speakers, start=1):
        assignments.append("Hello, {}! You'll be assigned to room {}!".format(speaker, index))
    return assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
    
    for assignment in assignments:
        print(assignment)

# Example usage
speakers_list = ["Arel", "Carol", "John", "Emma"]
printer(speakers_list)
