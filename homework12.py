class daily_note:
    def __init__(self):
        self.text = ""
    def fetch_text(self):
        self.text = input("provide text input: ")
    def show_text(self):
        print("text", self.text.upper())
user_note = daily_note()
user_note.fetch_text()
user_note.show_text()
class session_manager:
    def __init__(self):
        print("session has started")
    def __del__(self):
        print("session has finished")
def generate_session():
    print("initializing session")
    active_session = session_manager()
    print("session ready...")
    return active_session
print("")
print("calling generate_session() function")
session_instance = generate_session()
print("system active")
class digit_matcher:
    def locate_pair(self, digit_list, goal):
        cache = {}
        for idx, val in enumerate(digit_list):
            required = goal - val
            if required in cache:
                return (cache[required], idx)
            cache[val] = idx
        return None
digit_list = (100,67,98, 87, 1, 0,124)
target_goal = int(input("enter target total to locate: "))
outcome = digit_matcher().locate_pair(digit_list, target_goal)
if outcome is not None:
    print("pos1=%d, pos2=%d" % outcome)
else:
    print("no matching pair found.")
del session_instance
print("execution complete")