
class Dog():
    def __init__(self, color, breed, image_path, name, birthday, height, alertFactor):
        self.color = color
        self.type = breed
        self.image_path = image_path
        self.name = name
        self.birthday = birthday
        if height < 20:
            self.size = "small"
        if height > 20 and height < 50:
            self.size = "medium"
        if height > 50:
            self.size = "large"

        self.alertness = alertFactor

    def warning(self, name, distance):
        print(f"Min distance to trigger: {self.alertness * 2}")
        if name != "Owner":
            if distance < (int(self.alertness) * 2):
                print(f"{self.name}: Barks. Finds an intruder too close")
            else:
                print(f"{self.name}: Stays calm. No intruders nearby")
        else:
            print("Dog recognises it's owner and stays calm.")



color_1 = "brown"
breed_1 = "."
image_path = ""
name = "Dog"
birthday = ""
height = 25

alertfactor = 10

dog = Dog(color_1,breed_1,image_path,name,birthday,height,alertfactor) 
        
dog.warning("Person", 10)
# make 3 dogs randomly and print their alert factor. Then a random value for a person to be close. Then we give their name, and if the person is
# not known by the dogs, and the intruder is too close for their alert factor, they will bark, if they do know the person / are too far away
# they will not bark
