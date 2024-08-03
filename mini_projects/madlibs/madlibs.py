class MadLibs:
    def __init__(self):
        self.promptList = [
            "Enter a colour: ",
            "Enter a plural noun: ",
            "Enter an action: "
        ]
        self.gamePara = """Roses are {}
{} are blue
Close your eyes, or I'll {} you"""
    def play(self):
        answers=[]
        for prompt in self.promptList:
            answers.append(input(prompt))
        
        self.publish(answers)
    def publish(self, answers):
        print(self.gamePara.format(*answers))
        


# def madLibs():
#     color = input("Enter a colour: ")
#     noun = input("Enter a plural noun: ")
#     action = input("Enter an action: ")

#     print("Roses are "+color)
#     print(noun+" are blue")
#     print("Close your eyes, or i'll "+action+" you")