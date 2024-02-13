from mesa import Agent, Model
from mesa.time import RandomActivation
import datetime
import subprocess

class MenuAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.menu_displayed = False  # Flag to track whether the menu has been displayed

    def check_time(self):
        current_time = datetime.datetime.now().time()
        return current_time

    def display_menu(self, current_time):
        if datetime.time(8, 0) <= current_time < datetime.time(11, 0):
            menu = ["Dosa - ₹25", "Idli - ₹25", "Puri - ₹30", "Vada - ₹25", "Omlette - ₹30", "Tea - ₹15", "Coffee - ₹15"]
        elif datetime.time(11, 0) <= current_time < datetime.time(15, 0):
            menu = ["Meals - ₹45", "Chole bhature - ₹35", "Naan - ₹15", "Chapathi - ₹15", "Juice - ₹35", "Noodles - ₹30", "Paneer sabzi - ₹25", "Egg - ₹10", "Sabzi - ₹25"]
        elif datetime.time(15, 0) <= current_time < datetime.time(17, 0):
            menu = ["Fries - ₹25", "Cheese balls ₹25", "Masala puri - ₹30", "Pani puri - ₹30", "Bhel puri - ₹30"]
        else:
            menu = ["Closed"]
        return menu

    def step(self):
        if not self.menu_displayed:
            current_time = self.check_time()
            menu = self.display_menu(current_time)
            print(f"Welcome to the Restaurant!")
            print(f"Current time: {current_time}")
            print("Menu:")
            for item in menu:
                print(f"- {item}")
            print("Enjoy your meal!\n")
            self.menu_displayed = True

class MenuModel(Model):
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            agent = MenuAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()

def main():
    num_agents = 1
    model = MenuModel(num_agents)

    for _ in range(5):
        model.step()

if __name__ == "__main__":
    main()
    script_name=r"D:\ASEB\Semester 3\Projects\AI\ai_agent\ai_agent\AI_client.py"
    subprocess.call(['python', script_name])